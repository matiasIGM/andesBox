from rest_framework import serializers
from andesRestApi.models import Envio, Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id', None)
        representation.pop('envio', None)
        return representation    

class EnvioSerializer(serializers.ModelSerializer):
    movimientos = MovimientoSerializer(many=True, read_only=True)

    class Meta:
        model = Envio
        exclude = ['id']