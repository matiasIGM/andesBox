from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string
from django.utils import timezone

class Envio(models.Model):
    numero_seguimiento = models.CharField(max_length=7, unique=True, editable=False, default='') # Número de seguimiento del envío
    amountPieces = models.IntegerField(default=0) # Cantidad de piezas del envío
    customerName = models.CharField(max_length=50, null=True) # Nombre del cliente que envia la encomienda
    creationDate = models.DateTimeField(default=timezone.now)  # Fecha de creación del envío
    baseOrigin = models.CharField(max_length=50, default="CD de distribución ENEA PUDAHUEL")  # Ubicación base de origen del envío
    receiverName = models.CharField(max_length=50, null=True)  # Nombre del destinatario
    receiveMail = models.CharField(max_length=100, null=True, blank=True) # Correo electrónico del destinatario
    receiverPhone = models.CharField(max_length=50, null=True) # Teléfono del destinatario
    receiverAddress = models.CharField(max_length=100, null=True) # Dirección del destinatario
    receiverDistrict = models.CharField(max_length=50, null=True) # Distrito o provincia del destinatario
    receiverCity = models.CharField(max_length=50, null=True) # Ciudad del destinatario
    receiverRegion = models.CharField(max_length=50, null=True) # Región del destinatario
    locationName = models.CharField(max_length=50, default="")  # Nombre de la ubicación
    patent = models.CharField(max_length=10, default="") # Patente del vehiculo que efectua el envío
    courierName = models.CharField(max_length=100, null=True) # Nombre del repartidor
    receiver = models.CharField(max_length=50, null=True)  # Nombre del receptor del envío
    
    # Definir opciones para el estado del envío
    ESTADO_EN_PREPARACION = 'En Preparación'
    ESTADO_EN_REPARTO = 'En Reparto'
    ESTADO_ENTREGADO = 'Entregado'

    ESTADO_ENVIO_CHOICES = (
        (ESTADO_EN_PREPARACION, 'En Preparación'),
        (ESTADO_EN_REPARTO, 'En Reparto'),
        (ESTADO_ENTREGADO, 'Entregado'),
    )

    estado_envio = models.CharField(max_length=20, choices=ESTADO_ENVIO_CHOICES, default=ESTADO_EN_PREPARACION)

    def __str__(self):
        return str(self.numero_seguimiento)

    def save(self, *args, **kwargs):
        if not self.numero_seguimiento:
            self.numero_seguimiento = get_random_string(length=7, allowed_chars='0123456789')
        return super().save(*args, **kwargs)


class Movimiento(models.Model):
    envio = models.ForeignKey(Envio, related_name='movimientos',default=None, on_delete=models.CASCADE) # Relación con el envío
    estado = models.CharField(max_length=20, choices=Envio.ESTADO_ENVIO_CHOICES) # Estado del movimiento
    ubicacion = models.CharField(max_length=50)  # Ubicación del movimiento
    fecha_hora = models.DateTimeField(default=timezone.now) # Fecha y hora del movimiento

    def __str__(self):
        return self.estado