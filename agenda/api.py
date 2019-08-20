from agenda.models import Cita, Reserva
from agenda.serializers import CitasSerializer, ReservasSerializer
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from transversal.models import Perfil, TipoCliente, Cliente, TipoProfesional, Profesional, Paciente
from datetime import datetime


class CitasViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitasSerializer

    @list_route()
    def disponibles(self, request):
        ahora = datetime.now()
        citas = Cita.objects.filter(fecha_citacion__gte=ahora).exclude(cupos=0)  # muestra las horas disponible

        serializer = self.get_serializer(citas, many=True)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def add(self, request):
        cliente = Cliente.objects.get(pk=request.data['cliente'])
        profesional = Profesional.objects.get(pk=request.data['profesional'])

        cita = Cita(
            cliente=cliente,
            profesional=profesional,
           # establecimiento=request.data['establecimiento'],
            fecha_citacion=request.data['fecha'],
            hora_citacion=request.data['hora'],
            cupos=request.data['cupos']
            # usuario = request.user
        )
        cita.save()

        return Response({'status': 'Cita cargada correctamente'})

    @detail_route(methods=['post'])
    def add_reserva(self, request, pk=None):
        cita = Cita.objects.get(pk=pk)

        try:
            paciente = Paciente.objects.get(rut=request.data['rut'])
            paciente.nombre = request.data['nombre']
            paciente.apellidos = request.data['apellidos']
            paciente.email = request.data['email']
            paciente.telefono = request.data['telefono']
            paciente.direccion = request.data['direccion']
            paciente.save()
        except Exception, e:
            paciente = Paciente(
                rut=request.data['rut'],
                nombre=request.data['nombre'],
                apellidos=request.data['apellidos'],
                email=request.data['email'],
                telefono=request.data['telefono'],
                direccion=request.data['direccion']
            )
            paciente.save()

        reserva = Reserva.objects.filter(cita=cita, paciente=paciente)
        if not reserva:
            reserva = Reserva(
                cita=cita,
                paciente=paciente
            )
            reserva.save()

            # cita.cupos = (cita.cupos -1) esto antes  el 0 lo coloque yo
            cita.cupos = 0

            cita.save()

            return Response({'status': 'Reserva realizada correctamente'})
        else:
            content = {'Lo sentimos, otro usuario agendo la Hora'}

            return Response({'status': content})


class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer

    @list_route()
    def pendientes(self, request):
        ahora = datetime.now()
        reservas = Reserva.objects.filter(cita__fecha_citacion__gte=ahora).exclude(es_cancelada=True)
        serializer = self.get_serializer(reservas, many=True)
        return Response(serializer.data)

    @list_route()
    def mis_pendientes(self, request):
        ahora = datetime.now()
        # reservas = Reserva.objects.filter(paciente__rut=request.GET['rut'], cita__fecha_citacion__gte=ahora, cita__hora_citacion__gte=ahora).exclude(es_cancelada=True)
        reservas = Reserva.objects.filter(paciente__rut=request.GET['rut'], cita__fecha_citacion__gte=ahora).exclude(
            es_cancelada=True)
        serializer = self.get_serializer(reservas, many=True)
        return Response(serializer.data)

    @list_route()
    def historicas(self, request):
        ahora = datetime.now()
        reservas = Reserva.objects.filter(Q(cita__fecha_citacion__lte=ahora) | Q(es_cancelada=True))
        serializer = self.get_serializer(reservas, many=True)
        return Response(serializer.data)

    @list_route()
    def mis_historicas(self, request):
        ahora = datetime.now()
        reservas = Reserva.objects.filter(
            Q(paciente__rut=request.GET['rut'], cita__fecha_citacion__lte=ahora, cita__hora_citacion__lte=ahora) | Q(
                paciente__rut=request.GET['rut'], es_cancelada=True))
        serializer = self.get_serializer(reservas, many=True)
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def cancel_reserva(self, request, pk=None):
        reserva = Reserva.objects.get(pk=pk)
        reserva.es_cancelada = True
        reserva.save()

        cita = Cita.objects.get(pk=reserva.cita.id)
        cita.cupos = cita.cupos + 1
        cita.save()

        return Response({'status': 'Reserva anulada correctamente'})

    @detail_route(methods=['post'])
    def set_campania(self, request, pk=None):
        reserva = Reserva.objects.get(pk=pk)
        reserva.contact_campania = request.data['campania']
        reserva.contact_status = request.data['status']
        reserva.save()

        return Response({'status': 'Reserva actualizada correctamente'})
