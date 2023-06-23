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
router.register(r'transacciones', views.TransaccionView, 'usuario')


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Tasks API")),
    path('products/', products, name='products'),
    path('exit/', views.exit, name="exit"),
   
    


]  