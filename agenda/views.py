# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-42 -*-
import json
import datetime
import time
import unicodedata
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User, Permission
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse
from agenda.models import Cita, Reserva
from django.conf import settings
from transversal.models import Perfil, TipoCliente, Cliente, TipoProfesional, Profesional, Paciente
import xlwt
from transversal import views as transversal_views, api as transversal_api, api_contactabilidad
# Create your views here.
def index(request):

	context = {'menu': 'agenda'}
	return render(request, 'agenda/index.html', context)

def reservar_cita(request):
	#fecha_dia = (datetime.datetime.now() - datetime.timedelta(1)).strftime ("%-d")
	context = {'menu': 'agenda'}
	return render(request, 'agenda/reservar_cita.html', context)

def mis_citas(request):

	context = {'menu': 'agenda'}
	return render(request, 'agenda/mis_citas.html', context)
#add jp#
def historial(request):
	context = {'menu': 'historial'}
	return render(request, 'historial/historial.html', context)




@login_required
def cargar(request):

	context = {'menu': 'cargar'}
	return render(request, 'cargar/index.html', context)

@login_required
def gestionar(request):

	context = {'menu': 'gestionar'}
	return render(request, 'gestionar/index.html', context)

def recordatorioCitas(request):
	print "inicio recordatorio de citas"
	#se obtienen las reservas
	maniana = datetime.date.today() + datetime.timedelta(1)
	print "mañana"
	print maniana
	recordatorio = Reserva.objects.filter(contact_status=1, es_cancelada=False, recordatorio=False, cita__fecha_citacion=maniana)
	print "recordatorio"
	print recordatorio
	if recordatorio:
		#dia_ayer = (datetime.date.today() - datetime.timedelta(1)).strftime("%-d")
		#ayer = datetime.date.today() - datetime.timedelta(1)
		hoy = datetime.date.today()
		print "hoy"
		print hoy
		#hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
		#se obtiene json con id campania
		campania = api_contactabilidad.create_campania_fn(136)
		print "campania"
		print campania
		#transformar de json a python
		resutado = json.loads(campania.content)
		print "resultado"
		print resutado['data']['id_campania']

		def elimina_tildes(s):
			return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

		for reserva in recordatorio:
			print "entra al for"
			#se obtiene la fecha de ayer de la cita (24 horas antes)
			fecha_citacion_ayer = reserva.cita.fecha_citacion - datetime.timedelta(1)

			print "fecha_citacion_ayer"
			print fecha_citacion_ayer
			print reserva.id
			#se compara si la fecha de la cita es igual a la fecha de ayer
			#validar si esta condicion es necesaria, que es de la primera iteracion
			if fecha_citacion_ayer == hoy:
				print "entra al if"
				hospital = reserva.cita.cliente.nombre
				fecha = reserva.cita.fecha_citacion
				hora = reserva.cita.hora_citacion
				nombre = reserva.paciente.nombre
				rut = reserva.paciente.rut
				telefono = reserva.paciente.telefono
				especialidad = reserva.cita.especialidad
				#diccionario
				parametros = {
					'campania': str(resutado['data']['id_campania']), 
					'id_externo': str(reserva.id),  
					'rut': str(rut), 
					'nombre': elimina_tildes(nombre),
					'telefono': int(telefono),
					'especialidad': elimina_tildes(especialidad),
					'fecha_citacion': fecha.strftime('%Y/%m/%d'),
					'hora_citacion': hora.strftime('%H:%M:%S'),
					'hospital': elimina_tildes(hospital),
				}
				print "parametros"
				print parametros
				if parametros:
					cita_enviada = api_contactabilidad.send_cita_fn(parametros)
					print "cita_enviada"
					print cita_enviada
					if cita_enviada:
						print "if cita_enviada actualiza estado a reserva"
						#se actualiza la reserva para que no vuelva a ser consultada si ya se envio como recordatorio
						Reserva.objects.filter(pk=reserva.id).update(recordatorio=True)

	context = {'menu': 'gestionar'}
	return render(request, 'gestionar/recordatorioCitas.html', context)

def export_citas_xls(request):
	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="Cita.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Cita')

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	date_format = xlwt.XFStyle()
	date_format.num_format_str = 'dd/m/yy'
	hora_format = xlwt.XFStyle()
	hora_format.num_format_str = 'hh:mm:ss'

	columns = ['Establecimiento', 'Profesional', 'Especialidad', 'Fecha Citacion', 'Hora Citacion', ]

	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num])

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	ahora = datetime.datetime.now()
	rows = Reserva.objects.filter(cita__fecha_citacion__gte=ahora).exclude(Q(es_cancelada=True) | Q(contact_status=None)).values_list('cita__cliente__nombre', 'cita__profesional__nombre', 'cita__especialidad', 'cita__fecha_citacion', 'cita__hora_citacion')
	#rows = Cita.objects.filter(fecha_citacion__gte=ahora).exclude(es_cancelada=True).values_list('cliente', 'profesional', 'especialidad', 'fecha_citacion', 'hora_citacion', 'cupos', 'es_cancelada')

	formatos = [xlwt.easyxf('font: name Times New Roman, bold on'),xlwt.easyxf('font: name Times New Roman, bold on'),xlwt.easyxf('font: name Times New Roman, bold on'), xlwt.easyxf(num_format_str='D-MM-YYYY'), xlwt.easyxf(num_format_str='hh:mm:ss')]
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], formatos[col_num])


	wb.save(response)
	return response
