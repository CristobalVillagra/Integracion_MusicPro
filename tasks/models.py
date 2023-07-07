from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    datacompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Usuario(models.Model):
    user = models.CharField(primary_key=True, max_length=255, verbose_name='usuario')
    contrasena = models.CharField(max_length=20)
    saldo = models.IntegerField(default=50000)

    def __str__(self):
        return self.user

class Transaccion(models.Model):
    nrotransaccion = models.AutoField(primary_key=True, verbose_name='nro de transaccion')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    estado = models.CharField(max_length=32, null=False, blank=False, default='esperando', verbose_name='estado')
    usuario_origen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacciones_enviadas')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transacciones_recibidas')

    def __str__(self):
        return str(self.nrotransaccion)

    
    
    
    
    