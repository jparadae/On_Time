from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from transversal.models import Perfil, TipoCliente, Cliente, TipoProfesional, Profesional, Paciente

# Register your models here.
admin.site.unregister(User)

class PerfilInline(admin.StackedInline):
	model = Perfil

class PerfilAdmin(UserAdmin):
	inlines = [PerfilInline]

	list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')

admin.site.register(User, PerfilAdmin)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'tipocliente', 'es_ws', 'es_activo')
	list_filter = ('es_activo', 'es_ws', 'tipocliente')
	search_fields = ('nombre', )

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TipoCliente)
admin.site.register(TipoProfesional)

class ProfesionalAdmin(admin.ModelAdmin):
	list_display = ('id', 'tipoprofesional', 'rut', 'nombre', 'apellidos')
	list_filter = ('tipoprofesional', )
	search_fields = ('rut', 'nombre', 'apellidos')

admin.site.register(Profesional, ProfesionalAdmin)

class PacienteAdmin(admin.ModelAdmin):
	list_display = ('id', 'rut', 'nombre', 'apellidos', 'email', 'telefono', 'direccion')
	search_fields = ('rut', 'nombre', 'apellidos', 'email', 'telefono', 'direccion')

admin.site.register(Paciente, PacienteAdmin)