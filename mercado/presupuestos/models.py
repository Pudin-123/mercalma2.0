from django.db import models

class Presupuesto(models.Model):
    producto = models.CharField(max_length=200)
    email = models.EmailField()
    mensaje = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Presupuesto para {self.producto} ({self.email})"

class TelegramLog(models.Model):
    chat_id = models.CharField(max_length=50)
    username = models.CharField(max_length=100, blank=True, null=True)
    mensaje = models.TextField()
    recibido_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Msg de {self.username or self.chat_id} - {self.recibido_en}"


# Create your models here.
