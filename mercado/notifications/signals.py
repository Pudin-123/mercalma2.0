from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_chat.models import ChatMessage
from .models import Notification
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=ChatMessage)
def create_message_notification(sender, instance, created, **kwargs):
    if created:
        # Determinar el destinatario (el otro participante de la conversación)
        recipient = instance.conversation.seller
        if instance.sender == instance.conversation.seller:
            recipient = instance.conversation.buyer
            
        if recipient != instance.sender:  # No notificar al remitente
            Notification.objects.create(
                recipient=recipient,
                notification_type='message',
                title='Nuevo mensaje',
                message=f'Tienes un nuevo mensaje de {instance.sender.username}',
                content_object=instance
            )