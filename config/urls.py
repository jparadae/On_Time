"""dacion_horas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from agenda import views as agenda_views, api as agenda_api
from django.conf.urls import url, include
from django.contrib import admin, auth
from rest_framework import routers
from transversal import views as transversal_views, api as transversal_api, api_contactabilidad

router = routers.DefaultRouter()
router.register(r'agenda/citas', agenda_api.CitasViewSet)
router.register(r'agenda/reservas', agenda_api.ReservasViewSet)
router.register(r'transversal/tipo-cliente', transversal_api.TipoClienteViewSet)
router.register(r'transversal/clientes', transversal_api.ClienteViewSet)
router.register(r'transversal/tipo-profesionales', transversal_api.TipoProfesionalViewSet)
router.register(r'transversal/profesionales', transversal_api.ProfesionalViewSet)
router.register(r'transversal/pacientes', transversal_api.PacienteViewSet)

urlpatterns = [

    #Definir que solo abra en http://127.0.0.1:8000/agenda/reservar/
    # url(r'^agenda/reservar/$', agenda_views.reservar_cita, name='detalle-cita'),
    url(r'^admin/', admin.site.urls),

    url(r'^$', agenda_views.index, name='home'),
    url(r'^agenda/$', agenda_views.index, name='agenda'),
    url(r'^agenda/reservar/$', agenda_views.reservar_cita, name='reservar-cita'),

    url(r'^agenda/mis-citas/$', agenda_views.mis_citas, name='mis-citas'),

    url(r'^cargar/citas/$', agenda_views.cargar, name='cargar'),
    url(r'^gestionar/$', agenda_views.gestionar, name='gestionar'),
    url(r'^historial/$', agenda_views.historial, name='historial'),
    url(r'^export/xls/$', agenda_views.export_citas_xls, name='export_citas_xls'),

    # API REST
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/contactabilidad/create-campania/$', api_contactabilidad.create_campania, name='api-contactabilidad-create-campania'),
    url(r'^api/contactabilidad/send-cita/$', api_contactabilidad.send_cita, name='api-contactabilidad-send-cita'), 
    url(r'^api/contactabilidad/cancel-cita/$', api_contactabilidad.cancel_cita, name='api-contactabilidad-cancel-cita'),

    # Python Social Auth URLs
	url('', include('social.apps.django_app.urls', namespace='social')),

    # Login URL
	url(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^accounts/changed_password/?$', auth.views.password_change),
	url(r'^logout/$', auth.views.logout, {'next_page': '/'}, name='logout'),

    #probar recordatorio
    url(r'^gestionar/recordatorioCitas/$', agenda_views.recordatorioCitas, name='recordatorioCitas'),
]
