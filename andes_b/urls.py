"""
URL configuration for andes_b project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from andesRestApi.views import EnvioListCreateView, EnvioRetrieveUpdateDestroyView, MovimientoListCreateView, MovimientoRetrieveUpdateDestroyView, EnvioByTrackingNumberView, eliminar_movimiento, create_envio, update_movimiento, obtener_datos
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView


# Configuración de la vista de documentación de la API

schema_view = get_schema_view(
   openapi.Info(
      title="AndesBox API",
      default_version='v1.0',
      description="API desarollada en DjangoRest",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ma.garcesm@duocuc.cl"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=[permissions.AllowAny],
)



# URLs de la aplicación

urlpatterns = [
    path('admin/', admin.site.urls), # URL del panel de administración

    # URLs de la API
    path('envios/', EnvioListCreateView.as_view(), name='envio-list-create'),# URL para listar y crear envíos
    path('envios/track/<str:tracking_number>/', EnvioByTrackingNumberView.as_view({'get': 'get_envio'}), name='envio-get'),# URL para obtener un envío por número de seguimiento
    path('movimientos/<str:numero_seguimiento>/', update_movimiento, name='envio-update'),# URL para actualizar un movimiento
    path('movimientos/<str:numero_seguimiento>/movimientos/<int:id>/', eliminar_movimiento, name='eliminar-movimiento'), # URL para eliminar un movimiento
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),# URL para ver la documentación de la API en Swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),# URL para ver la documentación de la API en ReDoc
    path('obtener-datos/', obtener_datos, name='obtener-datos'), # URL para obtener datos desde api integración externa
    path('envios/<str:numero_seguimiento>/', EnvioRetrieveUpdateDestroyView.as_view(), name='envio-retrieve-update-destroy-by-tracking'),

    # URLs de la API
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('repartidor/', TemplateView.as_view(template_name='repartidor.html'), name='repartidor'), # URL de la página del repartidor

]