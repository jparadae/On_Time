from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	run = models.CharField(max_length=10)
	telefono = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		verbose_name = "Perfil"
		verbose_name_plural = "Perfiles"

	def __unicode__(self):
		return "%s (%s %s)" % (self.usuario, self.usuario.first_name, self.usuario.last_name)

class TipoCliente(models.Model):
	nombre = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Tipo de Modulo"
		verbose_name_plural = "Tipos de Modulos"

	def __unicode__(self):
		return self.nombre

class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	tipocliente = models.ForeignKey(TipoCliente)
	es_ws = models.BooleanField(default=True)
	es_activo = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Modulo"
		verbose_name_plural = "Modulos"

	def __unicode__(self):
		return self.nombre

class TipoProfesional(models.Model):
	nombre = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Tipo de Subcategoria"
		verbose_name_plural = "Tipos de Subcategorias"

	def __unicode__(self):
		return self.nombre

class Profesional(models.Model):
	cliente = models.ForeignKey(Cliente)
	tipoprofesional = models.ForeignKey(TipoProfesional)
	rut = models.CharField(max_length=9, unique=True)
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Sub Categoria"
		verbose_name_plural = "Sub Categorias"

	def __unicode__(self):
		return "%s %s (%s)" % (self.nombre, self.apellidos, self.rut)

class Paciente(models.Model):
	rut = models.CharField(max_length=9, unique=True)
	nombre = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	telefono = models.CharField(max_length=20)
	direccion = models.CharField(max_length=200, null=True)

	class Meta:
		verbose_name = "Solicitante"
		verbose_name_plural = "Solicitantes"

	def __unicode__(self):
		return "%s %s (%s)" % (self.nombre, self.apellidos, self.rut)