from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from market.models import Product, CartItem
from .models import ActionLog

def safe_log_action(user, action, object_repr, extra=None):
    """Safely log actions; skip if table doesn't exist yet."""
    try:
        ActionLog.objects.create(
            user=user if getattr(user, 'is_authenticated', False) else None,
            action=action,
            object_repr=object_repr,
            extra=extra
        )
    except Exception as e:
        # Silently fail if ActionLog table doesn't exist (migrations not applied)
        pass

@receiver(post_save, sender=Product)
def log_product_save(sender, instance, created, **kwargs):
    user = getattr(instance, 'seller', None) or None
    safe_log_action(
        user=user,
        action='create' if created else 'update',
        object_repr=f'Product #{instance.pk} - {getattr(instance,"title","")}',
        extra={'price': str(getattr(instance,'price', '')), 'stock': getattr(instance,'stock', None)}
    )

@receiver(post_delete, sender=Product)
def log_product_delete(sender, instance, **kwargs):
    user = getattr(instance, 'seller', None) or None
    safe_log_action(
        user=user,
        action='delete',
        object_repr=f'Product #{instance.pk} - {getattr(instance,"title","")}'
    )

@receiver(post_save, sender=CartItem)
def log_cartitem_save(sender, instance, created, **kwargs):
    user = getattr(getattr(instance, 'cart', None), 'user', None)
    safe_log_action(
        user=user,
        action='purchase' if created else 'update',
        object_repr=f'CartItem #{instance.pk} - product {getattr(instance.product,"title","")} x {instance.quantity}',
        extra={'cart_id': getattr(instance.cart,'pk', None)}
    )

@receiver(post_delete, sender=CartItem)
def log_cartitem_delete(sender, instance, **kwargs):
    user = getattr(getattr(instance, 'cart', None), 'user', None)
    safe_log_action(
        user=user,
        action='delete',
        object_repr=f'CartItem #{instance.pk} - product {getattr(instance.product,"title","")}'
    )
