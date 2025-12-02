from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Category
import json

@login_required
@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            
            if not name:
                return JsonResponse({
                    'status': 'error',
                    'message': 'El nombre de la categoría es requerido'
                })
            
            # Verificar si la categoría ya existe
            if Category.objects.filter(name__iexact=name).exists():
                return JsonResponse({
                    'status': 'error',
                    'message': 'Esta categoría ya existe'
                })
            
            # Crear la nueva categoría
            category = Category.objects.create(name=name)
            
            return JsonResponse({
                'status': 'success',
                'message': 'Categoría creada exitosamente',
                'category': {
                    'id': category.id,
                    'name': category.name
                }
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Datos inválidos'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Método no permitido'
    }, status=405)
