appAgenda.service('apiAgenda',  ['$http', 'returnHttp', function($http, returnHttp){
	// Return public API
	return({
		getCitas: getCitas,
		getCitasDisponibles: getCitasDisponibles,
		addCita: addCita,
		addReserva: addReserva,
		getReservasPendientes: getReservasPendientes,
		getReservasHistoricas: getReservasHistoricas,
		getMisReservasPendientes: getMisReservasPendientes,
		getMisReservasHistoricas: getMisReservasHistoricas,
		cancelReserva: cancelReserva,
		setCampania: setCampania
	});
	
	function getCitas(){
		return $http({
				method: 'GET',
				url: '/api/agenda/citas/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getCitasDisponibles(){
		return $http({
				method: 'GET',
				url: '/api/agenda/citas/disponibles/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function addCita(data){
		return $http({
				method: 'POST',
				url: '/api/agenda/citas/add/?format=json',
				data: data
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function addReserva(data){
		return $http({
				method: 'POST',
				url: '/api/agenda/citas/' + data.cita + '/add_reserva/?format=json',
				data: data
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function cancelReserva(cita){
		return $http({
				method: 'POST',
				url: '/api/agenda/reservas/' + cita + '/cancel_reserva/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function setCampania(cita, campania, status){
		return $http({
				method: 'POST',
				url: '/api/agenda/reservas/' + cita + '/set_campania/?format=json',
				data: {'campania': campania, 'status' : status}
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getReservasPendientes(){
		return $http({
				method: 'GET',
				url: '/api/agenda/reservas/pendientes/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getReservasHistoricas(){
		return $http({
				method: 'GET',
				url: '/api/agenda/reservas/historicas/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getMisReservasPendientes(rut){
		return $http({
				method: 'GET',
				url: '/api/agenda/reservas/mis_pendientes/?format=json',
				params: {'rut': rut}
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getMisReservasHistoricas(rut){
		return $http({
				method: 'GET',
				url: '/api/agenda/reservas/mis_historicas/?format=json',
				params: {'rut': rut}
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

}]);