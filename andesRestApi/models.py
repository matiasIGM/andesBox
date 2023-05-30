from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string
from django.utils import timezone

class Envio(models.Model):
    numero_seguimiento = models.CharField(max_length=7, unique=True, editable=False, default='')
    amountPieces = models.IntegerField(default=0)
    customerName = models.CharField(max_length=50, null=True)
    creationDate = models.DateTimeField(default=timezone.now)
    baseOrigin = models.CharField(max_length=50, default="CD de distribución ENEA PUDAHUEL")
    receiverName = models.CharField(max_length=50, null=True)
    receiveMail = models.CharField(max_length=100, null=True, blank=True)
    receiverPhone = models.CharField(max_length=50, null=True)
    receiverAddress = models.CharField(max_length=100, null=True)
    receiverDistrict = models.CharField(max_length=50, null=True)
    receiverCity = models.CharField(max_length=50, null=True)
    receiverRegion = models.CharField(max_length=50, null=True)
    locationName = models.CharField(max_length=50, default="")
    patent = models.CharField(max_length=10, default="")
    courierName = models.CharField(max_length=100, null=True)
    receiver = models.CharField(max_length=50, null=True)
    isDeliveryRetry = models.BooleanField(default=False)
    #movimientos = models.ManyToManyField('Movimiento', related_name='envios')

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
        return self.numero_seguimiento

    def save(self, *args, **kwargs):
        if not self.numero_seguimiento:
            self.numero_seguimiento = get_random_string(length=7, allowed_chars='0123456789')
        return super().save(*args, **kwargs)


class Movimiento(models.Model):
    envio = models.ForeignKey(Envio, related_name='movimientos',default=None, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=Envio.ESTADO_ENVIO_CHOICES)
    ubicacion = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.estado