appAgenda.service('apiTransversal',  ['$http', 'returnHttp', function($http, returnHttp){
	// Return public API
	return({
		getClientes: getClientes,
		getProfesionales: getProfesionales,
		getPacientes: getPacientes,
		getPacientePorRut: getPacientePorRut
	});
	
	function getClientes(){
		return $http({
				method: 'GET',
				url: '/api/transversal/clientes/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getProfesionales(){
		return $http({
				method: 'GET',
				url: '/api/transversal/profesionales/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getPacientes(){
		return $http({
				method: 'GET',
				url: '/api/transversal/pacientes/?format=json'
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

	function getPacientePorRut(rut){
		return $http({
				method: 'GET',
				url: '/api/transversal/pacientes/por_rut/?format=json',
				params: {'rut': rut}
			}).then(returnHttp.handleSuccess, returnHttp.handleError);
	}

}]);