appAgenda.service('apiContactabilidad',  ['$http', 'returnHttp', function($http, returnHttp){
	// Return public API
	return({
		createCampania: createCampania,
		sendCita: sendCita,
		cancelCita: cancelCita
	});

	function createCampania(tipo_campania){
		return $http({
				method: 'POST',
				url: '/api/contactabilidad/create-campania/',
				params: {'tipo': tipo_campania}
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function sendCita(id_campania, id_externo, rut_paciente, nombre_paciente, telefono_1, especialidad, fecha_citacion, hora_citacion, rut_medico, nombres_medico, texto_libre){
		return $http({
				method: 'POST',
				url: '/api/contactabilidad/send-cita/',
				params: {'campania': id_campania, 'externo': id_externo, 'rut_paciente': rut_paciente, 'nombre_paciente': nombre_paciente, 'telefono_1': telefono_1, 'especialidad': especialidad, 'fecha_citacion': fecha_citacion, 'hora_citacion': hora_citacion, 'rut_medico': rut_medico, 'nombres_medico': nombres_medico, 'texto_libre': texto_libre }
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function cancelCita(id_campania, id_externo, rut_paciente, nombre_paciente, telefono_1, especialidad, fecha_citacion, hora_citacion, rut_medico, nombres_medico, texto_libre){
		return $http({
				method: 'POST',
				url: '/api/contactabilidad/cancel-cita/',
				params: {'campania': id_campania, 'externo': id_externo, 'rut_paciente': rut_paciente, 'nombre_paciente': nombre_paciente, 'telefono_1': telefono_1, 'especialidad': especialidad, 'fecha_citacion': fecha_citacion, 'hora_citacion': hora_citacion, 'rut_medico': rut_medico, 'nombres_medico': nombres_medico, 'texto_libre': texto_libre }
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

}]);
