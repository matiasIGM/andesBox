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

from andesRestApi.views import EnvioListCreateView, EnvioRetrieveUpdateDestroyView, MovimientoListCreateView, MovimientoRetrieveUpdateDestroyView, EnvioByTrackingNumberView, create_envio, update_movimiento

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=[permissions.AllowAny],
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('envios/', EnvioListCreateView.as_view(), name='envio-list-create'),
    path('envios/<int:pk>/', EnvioRetrieveUpdateDestroyView.as_view(), name='envio-retrieve-update-destroy'),
    # path('movimientos/', MovimientoListCreateView.as_view(), name='movimiento-list-create'),
    # path('movimientos/<int:pk>/', MovimientoRetrieveUpdateDestroyView.as_view(), name='movimiento-retrieve-update-destroy'),
    path('envios/track/<str:tracking_number>/', EnvioByTrackingNumberView.as_view({'get': 'get_envio'}), name='envio-get'),
    #  path('movimientos/<str:numero_seguimiento>/', update_movimiento, name='envio-update'),
    path('movimientos/<str:numero_seguimiento>/', update_movimiento, name='envio-update'),
    path('envios/create/', create_envio, name='envio-create'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]