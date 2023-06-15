from rest_framework import serializers, generics, status, viewsets
from rest_framework.response import Response
from andesRestApi.models import Envio, Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('envio', None)# Comentario: Se omite la representación del campo 'envio' en el response de el modelo Movimientos
        return representation    

class EnvioSerializer(serializers.ModelSerializer):
    movimientos = MovimientoSerializer(many=True, read_only=True)

    class Meta:
        model = Envio
        exclude = ['id'] # Comentario: Se excluye el campo 'id' de la representación

    