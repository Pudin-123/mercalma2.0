from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Notification
import os
import logging

logger = logging.getLogger(__name__)

@login_required
def notification_list(request):
    try:
        notifications = request.user.notifications.all()[:50]
        unread_count = request.user.notifications.filter(read=False).count()
        
        # Debug: verificar que el template existe
        template_path = 'notifications/notification_list.html'
        logger.info(f"Buscando template: {template_path}")
        
        # Si pide JSON (para carga AJAX), devolverlo
        if request.GET.get('format') == 'json':
            data = {
                'notifications': [
                    {
                        'id': n.id,
                        'title': n.title,
                        'message': n.message,
                        'created_at': n.created_at.isoformat(),
                        'read': n.read,
                        'url': n.get_absolute_url()
                    }
                    for n in notifications
                ],
                'unread_count': unread_count
            }
            return JsonResponse(data)
        
        return render(request, template_path, {
            'notifications': notifications,
            'unread_count': unread_count
        })
    except Exception as e:
        logger.error(f"Error en notification_list: {str(e)}", exc_info=True)
        raise

@login_required
def mark_notification_read(request, pk):
    notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notification.mark_as_read()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok'})
    
    return redirect(notification.get_absolute_url())

@login_required
def mark_all_read(request):
    request.user.notifications.filter(read=False).update(read=True)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok'})
    
    return redirect('notifications:list')

@login_required
def get_unread_count(request):
    count = request.user.notifications.filter(read=False).count()
    return JsonResponse({'count': count})