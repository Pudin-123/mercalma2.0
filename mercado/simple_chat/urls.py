from django.urls import path
from . import views

app_name = 'simple_chat'

urlpatterns = [
    path('conversations/', views.conversation_list, name='conversation_list'),
    path('conversations/<int:pk>/', views.conversation_detail, name='conversation_detail'),
    path('start/<int:product_id>/', views.start_conversation, name='start_conversation'),
]