from agenda.models import Cita, Reserva
from datetime import datetime, timedelta, date, time
from rest_framework import serializers
from transversal.models import Perfil, TipoCliente, Cliente, TipoProfesional, Profesional, Paciente

class TipoClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoCliente
		fields = ('url', 'id', 'nombre')

class ClienteSerializer(serializers.ModelSerializer):
	tipo = TipoClienteSerializer(source="tipocliente")

	class Meta:
		model = Cliente
		fields = ('url', 'id', 'nombre', 'tipo')

class TipoProfesionalSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoProfesional
		fields = ('url', 'id', 'nombre')

class ProfesionalSerializer(serializers.ModelSerializer):
	cliente = ClienteSerializer()
	tipo = TipoProfesionalSerializer(source="tipoprofesional")

	class Meta:
		model = Profesional
		fields = ('url', 'id', 'rut', 'nombre', 'apellidos', 'tipo', 'cliente')
		
class PacienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Paciente
		fields = ('url', 'id', 'rut', 'nombre', 'apellidos', 'email', 'telefono', 'direccion')

#class DetalleSeriadosSerializer(serializers.HyperlinkedModelSerializer):
#	producto = serializers.Field(source='seriado__nombre')
#	familia = serializers.Field(source='seriado__familia__nombre')
#	usuario = serializers.Field(source='usuario__username')
#	created = serializers.DateTimeField(format='%d-%m-%Y')
#	modified = serializers.DateTimeField(format='%d-%m-%Y')
#
#	class Meta:
#		model = MovimientoSeriado
#		fields = ('serie', 'producto', 'familia', 'condicion', 'guia_despacho', 'ticket', 'comercio', 'OT', 'usuario', 'created', 'modified', )