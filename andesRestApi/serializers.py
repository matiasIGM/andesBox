from rest_framework import serializers, generics, status, viewsets
from rest_framework.response import Response
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

    # def perform_create(self, serializer):
    #     envio = serializer.save()
    #     movimiento = Movimiento(estado='En preparación', ubicacion='', fecha_hora=envio.creationDate)
    #     movimiento.save()
    #     envio.movimientos.add(movimiento)

    #     response_data = {
    #         'numero_seguimiento': envio.numero_seguimiento,
    #         'amountPieces': envio.amountPieces,
    #         'customerName': envio.customerName,
    #         'creationDate': envio.creationDate,
    #         'baseOrigin': envio.baseOrigin,
    #         'receiverName': envio.receiverName,
    #         'movimientos': [{
    #             'estado': movimiento.estado,
    #             'ubicacion': movimiento.ubicacion,
    #             'fecha_hora': movimiento.fecha_hora
    #         }]
    #     }

    #     return Response(response_data, status=status.HTTP_201_CREATED)

    # def delete(self, request, *args, **kwargs):
    #     numero_seguimiento = request.data.get('numero_seguimiento')
    #     if numero_seguimiento:
    #         envio = self.get_object(numero_seguimiento)
    #         if envio:
    #             envio.delete()
    #             return Response(status=status.HTTP_204_NO_CONTENT)
    #         else:
    #             return Response({'error': 'Envío no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response({'error': 'Se requiere el número de seguimiento'}, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, *args, **kwargs):
    #     numero_seguimiento = request.data.get('numero_seguimiento')
    #     if numero_seguimiento:
    #         envio = self.get_object(numero_seguimiento)
    #         if envio:
    #             serializer = self.get_serializer(envio, data=request.data, partial=True)
    #             serializer.is_valid(raise_exception=True)
    #             self.perform_update(serializer)
    #             return Response(serializer.data)
    #         else:
    #             return Response({'error': 'Envío no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response({'error': 'Se requiere el número de seguimiento'}, status=status.HTTP_400_BAD_REQUEST)

    # def get_object(self, numero_seguimiento):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     obj = generics.get_object_or_404(queryset, numero_seguimiento=numero_seguimiento)
    #     self.check_object_permissions(self.request, obj)
    #     return obj