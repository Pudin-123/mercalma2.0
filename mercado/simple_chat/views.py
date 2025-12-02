from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import ChatConversation, ChatMessage
from market.models import Product
from django.contrib import messages
import json

@login_required
def conversation_list(request):
    """Lista todas las conversaciones del usuario."""
    conversations = ChatConversation.objects.filter(
        Q(buyer=request.user) | Q(seller=request.user)
    ).select_related('buyer', 'seller', 'product')
    
    return render(request, 'simple_chat/conversation_list.html', {
        'conversations': conversations
    })

from django.views.decorators.csrf import csrf_protect

@login_required
@csrf_protect
def conversation_detail(request, pk):
    """Muestra una conversación específica y permite enviar mensajes."""
    try:
        conversation = ChatConversation.objects.select_related(
            'buyer', 'seller', 'product'
        ).prefetch_related('messages__sender').get(pk=pk)
        
        # Verificar que el usuario sea parte de la conversación
        if request.user not in [conversation.buyer, conversation.seller]:
            messages.error(request, "No tienes permiso para ver esta conversación.")
            return redirect('simple_chat:conversation_list')
        
        # Marcar mensajes como leídos
        conversation.messages.filter(
            sender__in=[conversation.buyer, conversation.seller]
        ).exclude(sender=request.user).update(is_read=True)

        # Soportar petición AJAX para obtener mensajes nuevos (polling)
        if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                after = int(request.GET.get('after', 0) or 0)
            except (ValueError, TypeError):
                after = 0

            new_messages = conversation.messages.filter(id__gt=after).order_by('created_at')
            result = []
            for m in new_messages:
                result.append({
                    'id': m.id,
                    'text': m.text,
                    'sender': m.sender.username if m.sender else '',
                    'created_at': m.created_at.strftime('%d/%m/%Y %H:%M')
                })
            return JsonResponse({'messages': result})
        
        if request.method == 'POST':
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                try:
                    # Soportar tanto JSON como form-data (FormData)
                    message_text = ''
                    content_type = request.content_type or ''
                    if 'application/json' in content_type:
                        try:
                            data = json.loads(request.body.decode('utf-8') if isinstance(request.body, (bytes, bytearray)) else request.body)
                            message_text = data.get('message', '')
                        except json.JSONDecodeError:
                            return JsonResponse({'status': 'error', 'message': 'Datos JSON inválidos'}, status=400)
                    else:
                        # Form submissions (AJAX via FormData) will appear in request.POST
                        message_text = request.POST.get('message') or request.POST.get('text') or ''

                    message_text = (message_text or '').strip()
                    if not message_text:
                        return JsonResponse({'status': 'error', 'message': 'El mensaje no puede estar vacío'}, status=400)

                    message = ChatMessage.objects.create(
                        conversation=conversation,
                        sender=request.user,
                        text=message_text
                    )

                    return JsonResponse({
                        'status': 'ok',
                        'message': {
                            'id': message.id,
                            'text': message.text,
                            'sender': message.sender.username,
                            'created_at': message.created_at.strftime('%d/%m/%Y %H:%M')
                        }
                    })
                except Exception as e:
                    return JsonResponse({'status': 'error', 'message': 'Error al procesar el mensaje'}, status=500)
            else:
                text = request.POST.get('message', '').strip()
                if text:
                    message = ChatMessage.objects.create(
                        conversation=conversation,
                        sender=request.user,
                        text=text
                    )
                return redirect('simple_chat:conversation_detail', pk=pk)
        
        return render(request, 'simple_chat/conversation_detail.html', {
            'conversation': conversation,
            'chat_messages': conversation.messages.all().order_by('created_at')
        })
        
    except ChatConversation.DoesNotExist:
        messages.error(request, "La conversación no existe.")
        return redirect('simple_chat:conversation_list')
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect('simple_chat:conversation_list')

@login_required
def start_conversation(request, product_id):
    """Inicia una nueva conversación con el vendedor de un producto."""
    product = get_object_or_404(Product, pk=product_id)
    
    if request.user == product.seller:
        messages.error(request, "No puedes iniciar una conversación contigo mismo.")
        return redirect('market:product_detail', pk=product_id)
    
    conversation, created = ChatConversation.objects.get_or_create(
        buyer=request.user,
        seller=product.seller,
        product=product
    )
    
    return redirect('simple_chat:conversation_detail', pk=conversation.pk)
