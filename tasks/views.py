from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializer import TaskSerializer, UsuarioSerializer, TransaccionSerializer, UserLoginSerializer, UserRegisterSerializer
from .models import Task, Usuario, Transaccion
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
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

def crear_usuario(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        contrasena = request.POST.get('contrasena')
        saldo = request.POST.get('saldo')
        Usuario.objects.create(user=user, contrasena=contrasena, saldo=saldo)
        return redirect('user')
    return render(request, 'register.html')

def editar_usuario(request, user):
    user = Usuario.objects.get(user=user)
    if request.method == 'POST':
        user.user = request.POST.get('user')
        user.contrasena = request.POST.get('contrasena')
        user.saldo = request.POST.get('saldo')
        user.save()
        return redirect('user')
    return render(request, 'perfil.html', {'usuario': user})

def eliminar_usuario(request, user):
    user = Usuario.objects.get(user=user)
    if request.method == 'POST':
        user.delete()
        return redirect('user')
    return render(request, 'delete.html', {'usuario': user})


@api_view(['POST'])
def UserRegister (request):
     usr_entrante = request.data['user']
     pass_entrante = request.data['contrasena']
     url = 'login.html'
     response = requests.get(url)
     content = response.json()
     saldo_externo = content['saldo']
     try:
        newuser = Usuario(user=usr_entrante, contrasena=pass_entrante, saldo=saldo_externo)
        newuser.save()
        return redirect('/login/')
        
     except:
        return Response({'message':'No se pudo crear el usuario, revise bien los campos'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserView(request):
    usuario = request.user
    serializer = UsuarioSerializer(usuario)
    return Response({'user': serializer.data}, status=status.HTTP_200_OK)


def loginview(request):
	return render(request, 'login.html')
 
def registerview(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': UserCreationForm
        })
        
    else:
        if request.POST["contrasena1"] == request.POST["contrasena2"]:
            try:
                user = User.objects.create_user(
                    usuario=request.POST['user'], password=request.POST["contrasena1"])
                user.save()
                login(request,user),
                return redirect(perfilview)            
            except IntegrityError:
                return render(request, 'login.html', {
                    'form': UserCreationForm,
                    "error": 'User alredy exist'
                })
                
        return render(request, 'login.html', {
            'form': UserCreationForm,
            "error": 'password do not match'
            
        })
    

def products (request): 
    return render(request, 'core/products.html')

def perfilview(request):
    usuario = request.session['user']
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

def user(request):
    user = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': user})

def transacciones(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'tasks/transacciones.html', {'transacciones': transacciones})