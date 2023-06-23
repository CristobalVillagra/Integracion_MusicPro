from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializer import TaskSerializer, UsuarioSerializer, TransaccionSerializer, UserLoginSerializer, UserRegisterSerializer
from .models import Task, Usuario, Transaccion
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
import json
import requests


# Create your views.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class TransaccionView(viewsets.ModelViewSet):
    serializer_class = TransaccionSerializer
    queryset = Transaccion.objects.all()




def index(request):
    return render(request, 'core/index.html')


def home(request):
    return render(request, 'core/home.html')

@login_required
def registerview(request):
      return render(request, 'core/base.html')

def loginview(request):
	return render(request, 'registration/login.html')

def products (request): 
    return render(request, 'core/products.html')

def perfilview(request):
    usuario = request.session['usuario']
    usr_encontrado = Usuario.objects.get(user = usuario)
    dinero_usuario = usr_encontrado.saldo
    response = requests.get(url, timeout=10)    
    content = response.json()
    saludoentrante = content['message']
    print(usr_encontrado)
    return render(request, 'perfil.html', {'user': usr_encontrado.user, 'saldo': dinero_usuario, 'saludo': saludoentrante})

def saludo(request):
    response = requests.get(url)
    content = response.json()

    print(content['message'])
    return HttpResponse(content)

def exit(request):
    logout(request)
    return redirect('home')