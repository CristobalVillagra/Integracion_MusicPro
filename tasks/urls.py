from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks import views
from .views import *

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')
router.register(r'usuarios', views.UsuarioView, 'usuario')
router.register(r'transacciones', views.TransaccionView, 'transacciones')

app_name = 'tasks'

urlpatterns = [       
                                  
    path('',homeApi), 
    path('', views.registerview),
    path('login/', views.registerview),
    path("api/v1/", include(router.urls)),                       
    path('docs/', include_docs_urls(title="Tasks API")),
    path('perfil/', views.perfilview),
    path('api/tasks/', views.TaskView.as_view({'get': 'list', 'post': 'create'}), name='task-list'),
    path('api/tasks/<int:pk>/', views.TaskView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task-detail'),
    path('api/usuarios/', views.UsuarioView.as_view({'get': 'list', 'post': 'create'}), name='usuario-list'),
    path('api/usuarios/<int:pk>/', views.UsuarioView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='usuario-detail'),
    path('api/transacciones/', views.TransaccionView.as_view({'get': 'list', 'post': 'create'}), name='transaccion-list'),
    path('api/transacciones/<int:pk>/', views.TransaccionView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='transaccion-detail'),
    path('api/user/register/', views.UserRegister, name='user-register'),
    path('api/user/login/', views.UserLogin, name='user-login'),
    path('api/transferencia/', views.transferencia_api, name='transferencia-api'),
    path('transaccion/', views.transferencia_view, name='transaccion'),
    path('user/logout/', views.UserLogout, name='user-logout'),
    path('user/view/', views.UserView, name='user-view'),
    path('home/', views.homeApi, name='home-api'),
    path('register/', views.registerview, name='register'),
    path('login/', views.loginview, name='login'),
    path('perfil/', views.perfilview, name='perfil'),
    path('saludo/', views.saludo, name='saludo'),
    path('beatpayform/', views.beatpayform, name='beatpay-form'),
    path('beatpay/', views.beatpay, name='beatpay'),
    path('webpay/', views.webpay, name='webpay'),
    path('webpay/respuesta/', views.webpay_respuesta, name='webpay-respuesta'),
    path('transaccionpage/', transaccion_view, name='transaccionpage'),
    path('transferirbeatpay/', beatpay, name='transferirbeatpay'),
    
]

