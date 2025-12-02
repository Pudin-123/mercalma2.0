from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('create/', views.create_category, name='create_category'),
]