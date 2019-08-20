from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from transversal.models import Perfil, TipoCliente, Cliente, TipoProfesional, Profesional, Paciente
from transversal.serializers import TipoClienteSerializer, ClienteSerializer, TipoProfesionalSerializer, ProfesionalSerializer, PacienteSerializer

class TipoClienteViewSet(viewsets.ModelViewSet):
	queryset = TipoCliente.objects.all()
	serializer_class = TipoClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.filter(es_activo=True)
	serializer_class = ClienteSerializer

class TipoProfesionalViewSet(viewsets.ModelViewSet):
	queryset = TipoProfesional.objects.all()
	serializer_class = TipoProfesionalSerializer

class ProfesionalViewSet(viewsets.ModelViewSet):
	queryset = Profesional.objects.all()
	serializer_class = ProfesionalSerializer

class PacienteViewSet(viewsets.ModelViewSet):
	queryset = Paciente.objects.all()
	serializer_class = PacienteSerializer

	@list_route()
	def por_rut(self, request):
		try:
			paciente = Paciente.objects.get(rut=request.GET['rut'])
			serializer = self.get_serializer(paciente)
			return Response(serializer.data)			
		
		except Exception, e:
			return Response({'status': 404, 'message': 'Solicitante no encontrado.'}, status=status.HTTP_404_NOT_FOUND)