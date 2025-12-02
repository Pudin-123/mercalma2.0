from django.db import models
from django.conf import settings
from django.urls import reverse
from market.models import Product
from django.utils import timezone

class ChatConversation(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='buyer_conversations', on_delete=models.CASCADE)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='seller_conversations', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-updated_at']
        unique_together = ['buyer', 'seller', 'product']

    def get_absolute_url(self):
        return reverse('simple_chat:conversation_detail', args=[self.pk])

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

class ChatMessage(models.Model):
    conversation = models.ForeignKey(ChatConversation, related_name='messages', on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']