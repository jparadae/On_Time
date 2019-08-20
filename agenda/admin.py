from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from agenda.models import Cita, Reserva
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
#import datetime

# Register your models here.
class CitaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('id', 'cliente', 'profesional', 'fecha_citacion', 'hora_citacion', 'cupos', 'es_cancelada')
	import_id_fields = ('id',)
	exclude = ('id', 'created',)
	list_filter = ('es_cancelada', 'cliente', 'profesional')
	search_fields = ('cliente', 'profesional')

#class CitaResource(resources.ModelResource):
#	fecha_citacion = DateField(input_formats=['%Y-%m-%d'])
#	class Meta:
#		model = Cita
		#fecha_citacion = fields.Field(column_name='fecha_citacion', widget=DateWidget(format = '% Y - % m - % d'))
#		skip_unchanged = True
#		report_skipped = True
#		import_id_fields = ('id',)
		#exclude = ('id',)
#		fields = ('id','cliente__nombre', 'especialidad', 'profesional__nombre', 'profesional__apellidos', 'fecha_citacion', 'hora_citacion', 'cupos', )
#		export_order = ('id','cliente__nombre', 'especialidad', 'profesional__nombre', 'profesional__apellidos', 'fecha_citacion', 'hora_citacion', 'cupos', )
		#widgets = {
		#	'fecha_citacion': forms.DateInput(format=('%Y-%m-%d')),
		#}
#class CitaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#	resource_class = CitaResource

admin.site.register(Cita, CitaAdmin)

#class ReservaResource(resources.ModelResource):
#	model = Reserva
#	class Meta:
#		fields = ('id', 'cita__cliente__nombre', 'cita__especialidad', 'cita__profesional__nombre', 'cita__fecha_citacion', 'cita__hora_citacion', 'paciente__nombre', 'paciente__apellidos', 'cita__cupos', )

#class ReservaAdmin(ImportExportModelAdmin):
#	resource_class = ReservaResource

class ReservaAdmin(admin.ModelAdmin):
	#list_display = ('id', 'get_cliente', 'get_especialidad', 'get_profesional', 'get_fecha_citacion', 'get_hora_citacion', 'paciente', 'get_cupos', 'es_cancelada',)
	list_display = ('id', 'cita', 'paciente', 'es_cancelada',)

	#list_filter = ('es_cancelada', 'paciente')
	search_fields = ('id', 'paciente__nombre')

	#def get_cliente(self, obj):
	#	return obj.cita.cliente
	#get_cliente.short_description = 'Establecimiento'
	#get_cliente.admin_order_field = 'cita__cliente'

	#def get_profesional(self, obj):
	#	return obj.cita.profesional
	#get_profesional.short_description = 'Profesional'
	#get_profesional.admin_order_field = 'cita__profesional'

	#def get_especialidad(self, obj):
	#	return obj.cita.especialidad
	#get_especialidad.short_description = 'Especialidad'
	#get_especialidad.admin_order_field = 'cita__especialidad'

	#def get_fecha_citacion(self, obj):
	#	return obj.cita.fecha_citacion
	#get_fecha_citacion.short_description = 'Fecha de Citacion'
	#get_fecha_citacion.admin_order_field = 'cita__fecha_citacion'

	#def get_hora_citacion(self, obj):
	#	return obj.cita.hora_citacion
	#get_hora_citacion.short_description = 'Hora'
	#get_hora_citacion.admin_order_field = 'cita__hora_citacion'

	#def get_cupos(self, obj):
	#	return obj.cita.cupos
	#get_cupos.short_description = 'Cupos'
	#get_cupos.admin_order_field = 'cita__cupos'

admin.site.register(Reserva, ReservaAdmin)