from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render
from requests.auth import HTTPDigestAuth
import json, requests

# Create your views here.
credenciales = {'user': 'dacion_horas', 'pass': 'dacion_horas.-2016'}

@login_required
def create_campania(request):
	#url = 'http://10.8.255.106/api/citas/crear_campania/?id_tipo=%s' % (request.GET['tipo'])
	url = 'http://10.8.255.53/api/citas/crear_campania/?id_tipo=%s' % (request.GET['tipo'])
	result = requests.get(url, auth=HTTPDigestAuth(credenciales['user'], credenciales['pass']))

	response_data = {'status': True, 'data': result.json()}
	return HttpResponse(json.dumps(response_data), content_type='application/json')
	
@login_required
def send_cita(request):
	#url = 'http://10.8.255.106/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (request.GET['campania'], request.GET['externo'], request.GET['nombre_paciente'], request.GET['telefono_1'], request.GET['especialidad'], request.GET['fecha_citacion'], request.GET['hora_citacion'], request.GET['texto_libre'])
	url = 'http://10.8.255.53/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (request.GET['campania'], request.GET['externo'], request.GET['nombre_paciente'], request.GET['telefono_1'], request.GET['especialidad'], request.GET['fecha_citacion'], request.GET['hora_citacion'], request.GET['texto_libre'])
	result = requests.get(url, auth=HTTPDigestAuth(credenciales['user'], credenciales['pass']))
	
	response_data = {'status': True, 'data': result.json()}
	return HttpResponse(json.dumps(response_data), content_type='application/json')

@login_required
def cancel_cita(request):
	#url = 'http://10.8.255.106/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (request.GET['campania'], request.GET['externo'], request.GET['nombre_paciente'], request.GET['telefono_1'], request.GET['especialidad'], request.GET['fecha_citacion'], request.GET['hora_citacion'], request.GET['texto_libre'])
	url = 'http://10.8.255.53/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (request.GET['campania'], request.GET['externo'], request.GET['nombre_paciente'], request.GET['telefono_1'], request.GET['especialidad'], request.GET['fecha_citacion'], request.GET['hora_citacion'], request.GET['texto_libre'])
	result = requests.get(url, auth=HTTPDigestAuth(credenciales['user'], credenciales['pass']))

	response_data = {'status': True, 'data': result.json()}
	return HttpResponse(json.dumps(response_data), content_type='application/json')

def create_campania_fn(tipo):
	#url = 'http://10.8.255.106/api/citas/crear_campania/?id_tipo=%s' % (request.GET['tipo'])
	url = 'http://10.8.255.53/api/citas/crear_campania/?id_tipo=%s' % (tipo)
	result = requests.get(url, auth=HTTPDigestAuth(credenciales['user'], credenciales['pass']))

	response_data = {'status': True, 'data': result.json()}
	return HttpResponse(json.dumps(response_data), content_type='application/json')

def send_cita_fn(parametros):
	#url = 'http://10.8.255.106/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (request.GET['campania'], request.GET['externo'], request.GET['nombre_paciente'], request.GET['telefono_1'], request.GET['especialidad'], request.GET['fecha_citacion'], request.GET['hora_citacion'], request.GET['texto_libre'])
	url = 'http://10.8.255.53/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (parametros['campania'],parametros['id_externo'], parametros['nombre'], parametros['telefono'], parametros['especialidad'], parametros['fecha_citacion'], parametros['hora_citacion'], parametros['hospital'])
	print url
	result = requests.get(url, auth=HTTPDigestAuth(credenciales['user'], credenciales['pass']))
	print result
	response_data = {'status': True, 'data': result.json()}
	return HttpResponse(json.dumps(response_data), content_type='application/json')

@login_required
def cancel_cita_fn(request):
	#url = 'http://10.8.255.106/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (request.GET['campania'], request.GET['externo'], request.GET['nombre_paciente'], request.GET['telefono_1'], request.GET['especialidad'], request.GET['fecha_citacion'], request.GET['hora_citacion'], request.GET['texto_libre'])
	url = 'http://10.8.255.53/api/citas/enviar/?id_campania=%s&id_externo=%s&nombre_paciente=%s&telefono_1=%s&especialidad=%s&fecha_citacion=%s&hora_citacion=%s&texto_libre=%s' % (request.GET['campania'], request.GET['externo'], request.GET['nombre_paciente'], request.GET['telefono_1'], request.GET['especialidad'], request.GET['fecha_citacion'], request.GET['hora_citacion'], request.GET['texto_libre'])
	result = requests.get(url, auth=HTTPDigestAuth(credenciales['user'], credenciales['pass']))

	response_data = {'status': True, 'data': result.json()}
	return HttpResponse(json.dumps(response_data), content_type='application/json')