from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('message', 'Nuevo mensaje'),
        ('sale', 'Nueva venta'),
        ('purchase', 'Nueva compra'),
    )

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    # Para referenciar cualquier modelo (Product, ChatMessage, etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', 'read', 'created_at']),
        ]

    def __str__(self):
        return f"{self.get_notification_type_display()} para {self.recipient.username}"

    def get_absolute_url(self):
        if self.notification_type == 'message':
            if hasattr(self.content_object, 'conversation'):
                return reverse('simple_chat:conversation_detail', args=[self.content_object.conversation.id])
        elif self.notification_type in ['sale', 'purchase']:
            return reverse('market:order_detail', args=[self.object_id])
        return '#'

    def mark_as_read(self):
        self.read = True
        self.save()