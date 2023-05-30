from rest_framework import serializers
from andesRestApi.models import Envio, Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'

class EnvioSerializer(serializers.ModelSerializer):
    movimientos = MovimientoSerializer(many=True, read_only=True)

    class Meta:
        model = Envio
        exclude = ['id']