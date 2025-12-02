from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
from django.conf import settings
from rest_framework import viewsets, permissions
from django.core.exceptions import PermissionDenied
import mercadopago
from django.contrib import messages
from .models import Product, Category

from .models import Product, Cart, CartItem
from .serializers import ProductSerializer
from .forms import ProductForm

# --- UPDATE CART ---
@login_required
def update_cart(request):
    """Actualiza las cantidades de los productos en el carrito"""
    cart = Cart.objects.get_or_create(user=request.user)[0]

    for key, value in request.POST.items():
        if key.startswith("quantity_"):
            try:
                product_id = key.split("_")[1]
                quantity = int(value)
                if quantity > 0:
                    cart_item, created = CartItem.objects.get_or_create(
                        cart=cart,
                        product_id=product_id,
                    )
                    cart_item.quantity = quantity
                    cart_item.save()
                else:
                    CartItem.objects.filter(cart=cart, product_id=product_id).delete()
            except (ValueError, Product.DoesNotExist):
                continue

    return redirect("market:cart_detail")

# --- CREAR ORDEN ---
@login_required
def create_order(request):
    """Crea una orden a partir del carrito."""
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        return redirect("market:cart_detail")

    # Calcular total
    total = sum(item.product.price * item.quantity for item in cart.items.all())

    # Acá podrías guardar el pedido real si tuvieras el modelo Order
    print(f"Orden creada para {request.user.username} por ${total}")

    # Vaciar carrito después de la orden
    cart.items.all().delete()

    provider = request.POST.get("provider", "stripe")
    if provider == "stripe":
        return redirect("market:payment_success")
    elif provider == "mp":
        return redirect("market:payment_success")
    else:
        return redirect("market:payment_cancel")

# --- API REST ---

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


# --- PRODUCTOS ---
@login_required
def product_detail(request, pk):
    """Vista para mostrar los detalles de un producto."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "market/product_detail.html", {"product": product})

@login_required
def my_products(request):
    # Filtramos productos creados por el usuario actual
    products = Product.objects.filter(seller=request.user).order_by("-created_at")
    return render(request, "market/my_products.html", {"products": products})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Solo el vendedor puede eliminar
    if product.seller != request.user:
        raise PermissionDenied("No tenés permiso para eliminar este producto.")

    if request.method == "POST":
        product.delete()
        messages.success(request, "El producto fue eliminado correctamente.")
        return redirect("market:product_list")

    return render(request, "market/delete_product_confirm.html", {"product": product})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Solo el vendedor puede editar
    if product.seller != request.user:
        raise PermissionDenied("No tenés permiso para editar este producto.")

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("market:product_detail", pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, "market/edit_product.html", {"form": form, "product": product})

from django.db import transaction

@login_required
def create_product(request):
    """Permite crear un producto nuevo"""
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    product = form.save(commit=False)
                    product.seller = request.user
                    product.save()
                    messages.success(request, 'Producto creado exitosamente')
                    return redirect("market:product_list")
            except Exception as e:
                messages.error(request, f"Error al crear el producto: {str(e)}")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")
    else:
        form = ProductForm()

    return render(request, "market/product_form.html", {
        "form": form,
        "title": "Crear Producto",
        "submit_label": "Crear Producto"
    })

@login_required
def product_list(request):
    categories = Category.objects.all()
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    category = request.GET.get('category', '').lower()

    # Filtramos los productos
    products = Product.objects.select_related('seller', 'category').filter(active=True)

    # Mapeo de categorías de URL a nombres en la base de datos
    category_mapping = {
        'supermercado': ['Supermercado', 'Alimentos'],  # Mostrar productos de Alimentos en Supermercado
        'tecnologia': 'Tecnología',
        'hogar': 'Hogar',
        'moda': 'Moda',
        'deportes': 'Deportes',
        'ofertas': 'Ofertas'
    }

    if query:
        products = products.filter(title__icontains=query)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if category and category in category_mapping:
        if isinstance(category_mapping[category], list):
            # Si es una lista de categorías (como en el caso de supermercado)
            products = products.filter(category__name__in=category_mapping[category])
        else:
            # Si es una única categoría
            products = products.filter(category__name=category_mapping[category])

    return render(request, "market/product_list.html", {
        "products": products,
        "q": query,
        "min_price": min_price,
        "max_price": max_price,
        "category": category,
        "categories": categories
    })


@login_required
def product_detail(request, pk):
    """Muestra el detalle de un producto."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "market/product_detail.html", {"product": product})


@login_required
def product_edit(request, pk):
    """Edita un producto propio."""
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("market:product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "market/product_form.html", {"form": form})


@login_required
def product_delete(request, pk):
    """Desactiva un producto."""
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == "POST":
        product.active = False
        product.save()
        return redirect("market:product_list")
    return render(request, "market/product_confirm_delete.html", {"product": product})


# --- CARRITO ---

@login_required
def cart_detail(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    items = cart.items.all()  # 👈 convertimos RelatedManager a queryset iterable
    total_price = sum(item.total_price for item in items)
    return render(request, "market/cart_detail.html", {
        "cart": cart,
        "items": items,
        "total_price": total_price,
    })


@login_required
def add_to_cart(request, product_id):
    """Agrega un producto al carrito."""
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()
    return redirect("market:cart_detail")


@login_required
def remove_from_cart(request, item_id):
    """Elimina un producto del carrito."""
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, "Producto eliminado del carrito.")
    return redirect("market:cart_detail")


@login_required
def clear_cart(request):
    """Vacía el carrito."""
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.items.all().delete()
    return redirect("market:cart_detail")

@login_required
def update_cart_ajax(request):
    """Actualiza cantidades de productos en el carrito vía AJAX"""
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")

        if not product_id or not quantity:
            return JsonResponse({
                "success": False,
                "error": "Faltan datos requeridos"
            }, status=400)

        try:
            quantity = int(quantity)
            if quantity < 1:
                return JsonResponse({
                    "success": False,
                    "error": "La cantidad debe ser mayor a 0"
                }, status=400)

            cart = Cart.objects.get_or_create(user=request.user)[0]
            
            # Intentamos obtener el item del carrito
            try:
                item = cart.items.get(product_id=product_id)
                item.quantity = quantity
                item.save()
            except CartItem.DoesNotExist:
                # Si el item no existe, verificamos que el producto exista
                product = get_object_or_404(Product, id=product_id)
                item = CartItem.objects.create(
                    cart=cart,
                    product=product,
                    quantity=quantity
                )

            # Calculamos los totales
            subtotal = float(item.product.price * item.quantity)
            total_price = float(sum(i.product.price * i.quantity for i in cart.items.all()))

            return JsonResponse({
                "success": True,
                "subtotal": subtotal,
                "total_price": total_price,
                "quantity": item.quantity,
            })
        except Product.DoesNotExist:
            return JsonResponse({
                "success": False,
                "error": "El producto no existe"
            }, status=404)
        except ValueError:
            return JsonResponse({
                "success": False,
                "error": "Cantidad inválida"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status=500)

    return JsonResponse({
        "success": False,
        "error": "Método no permitido"
    }, status=405)

# --- MERCADOPAGO ---

@login_required
def create_preference(request, product_id):
    sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    # Ejemplo: obtener producto
    from .models import Product
    product = Product.objects.get(id=product_id)

    preference_data = {
        "items": [
            {
                "title": product.title,
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": float(product.price),
            }
        ],
        "back_urls": {
            "success": "http://127.0.0.1:8000/payment/success/",
            "failure": "http://127.0.0.1:8000/payment/failure/",
            "pending": "http://127.0.0.1:8000/payment/pending/",
        },
        "auto_return": "approved",
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return JsonResponse({
        "id": preference["id"]
    })


def payment_success(request):
    """Página de pago exitoso."""
    return render(request, "market/payment_success.html")


def payment_cancel(request):
    """Página de pago fallido/cancelado."""
    return render(request, "market/payment_cancel.html")

# -- REDIRECCIÓN DESDE MY PRODUCTS ---
@login_required
def redirect_to_create_product(request):
    """Redirecciona a la vista principal de creación de productos"""
    return redirect("market:create_product")

@login_required
def mercadopago_checkout(request):
    """Crea una preferencia de Mercado Pago con todos los productos del carrito"""
    try:
        # Validar token
        access_token = settings.MERCADOPAGO_ACCESS_TOKEN
        
        if not access_token or not isinstance(access_token, str):
            messages.error(request, "Error: Token de MercadoPago no configurado correctamente.")
            return redirect("market:cart_detail")
        
        sdk = mercadopago.SDK(access_token)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()

        if not cart_items.exists():
            messages.warning(request, "Tu carrito está vacío.")
            return redirect("market:cart_detail")

        items = []
        total = 0

        for item in cart_items:
            items.append({
                "title": item.product.title,
                "quantity": int(item.quantity),
                "currency_id": "ARS",
                "unit_price": float(item.product.price),
            })
            total += float(item.product.price) * item.quantity

        preference_data = {
            "items": items,
            "back_urls": {
                "success": request.build_absolute_uri("/market/payment/success/"),
                "failure": request.build_absolute_uri("/market/payment/cancel/"),
                "pending": request.build_absolute_uri("/market/payment/cancel/"),
            },
            "external_reference": str(request.user.id),
        }

        preference_response = sdk.preference().create(preference_data)
        
        if preference_response.get("status") != 201:
            error_msg = preference_response.get("response", {}).get("message", "Error desconocido")
            messages.error(request, f"Error al generar la preferencia de pago: {error_msg}")
            return redirect("market:cart_detail")

        preference = preference_response.get("response", {})
        init_point = preference.get("init_point")

        if not init_point:
            messages.error(request, "Error: No se recibió URL de pago de MercadoPago")
            return redirect("market:cart_detail")

        # 👉 Opcional: limpiar carrito una vez creada la preferencia
        # cart.items.all().delete()

        return redirect(init_point)

    except Exception as e:
        print(f"ERROR en mercadopago_checkout: {str(e)}")
        import traceback
        traceback.print_exc()
        messages.error(request, f"Error con Mercado Pago: {str(e)}")
        return redirect("market:cart_detail")