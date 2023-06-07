from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from andesRestApi.models import Envio, Movimiento
from andesRestApi.serializers import EnvioSerializer, MovimientoSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from django.http import Http404

# class EnvioListCreateView(generics.ListCreateAPIView):
#     queryset = Envio.objects.all()
#     serializer_class = EnvioSerializer

#     def perform_create(self, serializer):
#         estado = self.request.data.get('estado_envio')
#         if estado == Envio.ESTADO_EN_REPARTO or estado == Envio.ESTADO_ENTREGADO:
#             envio = serializer.save()
#             movimiento_data = {
#                 'estado': estado,
#                 'ubicacion': self.request.META.get('REMOTE_ADDR'),
#                 'fecha_hora': timezone.now(),
#                 'envio': envio.id
#             }
#             Movimiento.objects.create(**movimiento_data)
#             return Response({'detail': 'Envío gestionado correctamente.'})
#         else:
#             return Response({'error': 'No se permite cambiar el estado a {}'.format(estado)},
#                             status=status.HTTP_400_BAD_REQUEST)
class EnvioListCreateView(generics.ListCreateAPIView):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

    def create(self, request, *args, **kwargs):
        estado_envio = request.data.get('estado_envio', Envio.ESTADO_EN_PREPARACION)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        envio = serializer.save(estado_envio=estado_envio)
        headers = self.get_success_headers(serializer.data)

        response_data = {
            'numero_seguimiento': envio.numero_seguimiento,
            'estado_envio': envio.estado_envio
        }

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)    


class EnvioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

class MovimientoListCreateView(generics.ListCreateAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer

class MovimientoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer



# class EnvioByTrackingNumberView(viewsets.ViewSet):
#     queryset = Envio.objects.all()
#     serializer_class = EnvioSerializer
#     lookup_field = 'numero_seguimiento'
#     lookup_url_kwarg = 'tracking_number'

#     def track(self, request, *args, **kwargs):
#         tracking_number = self.kwargs['tracking_number']
#         envio = get_object_or_404(Envio, numero_seguimiento=tracking_number)
#         serializer = self.serializer_class(envio)
#         return Response(serializer.data)
class EnvioByTrackingNumberView(viewsets.ViewSet):
    # ...
    
    @action(detail=True, methods=['get'])
    def get_envio(self, request, *args, **kwargs):
        tracking_number = self.kwargs['tracking_number']
        envio = get_object_or_404(Envio, numero_seguimiento=tracking_number)
        movimientos = Movimiento.objects.filter(envio=envio).order_by('-fecha_hora')

        movimientos_serializer = MovimientoSerializer(movimientos, many=True)

        response_data = {
            'numero_seguimiento': envio.numero_seguimiento,
            'amountPieces': envio.amountPieces,
            'customerName': envio.customerName,
            'creationDate': envio.creationDate,
            'baseOrigin': envio.baseOrigin,
            'receiverName': envio.receiverName,
            'receiveMail': envio.receiveMail,
            'receiverPhone': envio.receiverPhone,
            'receiverAddress': envio.receiverAddress,
            'receiverDistrict': envio.receiverDistrict,
            'receiverCity': envio.receiverCity,
            'receiverRegion': envio.receiverRegion,
            'locationName': envio.locationName,
            'patent': envio.patent,
            'courierName': envio.courierName,
            'receiver': envio.receiver,
            'isDeliveryRetry': envio.isDeliveryRetry,
            'estado_envio': envio.estado_envio,
            'movimientos': movimientos_serializer.data
        }

        return Response(response_data)


@api_view(['POST'])
def create_envio(request):
    serializer = EnvioSerializer(data=request.data)
    if serializer.is_valid():
        envio = serializer.save()
        return Response({
            'numero_seguimiento': envio.numero_seguimiento,
            'message': 'Envío gestionado de manera correcta.'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update_envio(request, pk):
#     estado = request.data.get('estado_envio')
#     if estado and (estado == Envio.ESTADO_EN_REPARTO or estado == Envio.ESTADO_ENTREGADO):
#         envio = get_object_or_404(Envio, pk=pk)
#         envio.estado_envio = estado
#         envio.save()
#         movimiento_data = {
#             'envio': envio,
#             'estado': estado,
#             'ubicacion': request.META.get('REMOTE_ADDR'),
#             'fecha_hora': timezone.now()
#         }
#         Movimiento.objects.create(**movimiento_data)
#         return Response({'detail': 'Envío gestionado correctamente.'})
#     else:
#         return Response({'error': 'No se permite cambiar el estado a {}'.format(estado)},
#                         status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_movimiento(request, numero_seguimiento):
    try:
        envio = Envio.objects.get(numero_seguimiento=numero_seguimiento)
    except Envio.DoesNotExist:
        return Response({"detail": "Envío no encontrado."}, status=404)

    estado = request.data.get('estado')
    ubicacion = request.data.get('ubicacion')
    fecha_hora = request.data.get('fecha_hora')

    movimiento = Movimiento(estado=estado, ubicacion=ubicacion, fecha_hora=fecha_hora, envio=envio)
    movimiento.save()

    # Actualizar los movimientos del envío
    envio.movimientos.add(movimiento)

    serializer = EnvioSerializer(envio)
    return Response(serializer.data, status=200)