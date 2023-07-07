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


urlpatterns = [                          
    path('', views.home, name='home'),
    path('', views.registerview),
    path('login/', views.registerview),
    path("api/v1/", include(router.urls)),                       
    path('docs/', include_docs_urls(title="Tasks API")),
    path('products/', products, name='products'),
    path('user/', views.user, name='usuarios'),
    path('transacciones/', views.transacciones, name='transacciones'),
    path('perfil/', views.perfilview),
    path('user/', views.user, name='usuarios'),
    path('user/crear/', views.crear_usuario, name='crear_usuario'),
    path('user/editar/<str:user>/', views.editar_usuario, name='editar_usuario'),
    path('user/eliminar/<str:user>/', views.eliminar_usuario, name='eliminar_usuario'),
    

]  