from django import forms
from .models import Product
from categorias.models import Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=True,
        empty_label="Selecciona una categoría",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'aria-label': 'Selecciona una categoría'
        }),
        help_text="Selecciona la categoría que mejor describa tu producto"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all().order_by('name')

    class Meta:
        model = Product
        fields = ["title", "description", "price", "image", "stock", "marca", "category"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "Nombre del producto",
                "required": "required"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control", 
                "rows": 3, 
                "placeholder": "Descripción breve"
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control", 
                "step": "any",
                "placeholder": "Precio (ejemplo: 54990)",
                "required": "required",
                "min": "0",
                "pattern": r"^\d+(\.\d{0,2})?$"
            }),
            "stock": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Cantidad disponible",
                "required": "required",
                "min": "1"
            }),
            "marca": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Marca del producto"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None:
            if price <= 0:
                raise forms.ValidationError("El precio debe ser mayor que cero")
            # Redondear a 2 decimales
            from decimal import Decimal
            price = Decimal(str(price)).quantize(Decimal('0.01'))
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 1:
            raise forms.ValidationError("El stock debe ser al menos 1")
        return stock