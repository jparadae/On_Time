from agenda.models import Cita, Reserva
from datetime import datetime, timedelta, date, time
from rest_framework import serializers
from transversal.models import Perfil, TipoCliente, Cliente, TipoProfesional, Profesional, Paciente
from transversal.serializers import ClienteSerializer, ProfesionalSerializer, PacienteSerializer

class CitasSerializer(serializers.ModelSerializer):
	cliente = ClienteSerializer()
	profesional = ProfesionalSerializer()

	class Meta:
		model = Cita
		fields = ('url', 'id', 'cliente', 'profesional', 'cliente', 'fecha_citacion', 'hora_citacion', 'cupos', 'es_cancelada')

class ReservasSerializer(serializers.ModelSerializer):
	cita = CitasSerializer()
	paciente = PacienteSerializer()

	class Meta:
		model = Reserva
		fields = ('url', 'id', 'cita', 'paciente', 'es_cancelada', 'contact_campania', 'contact_status')