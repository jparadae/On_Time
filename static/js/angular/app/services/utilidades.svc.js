appAgenda.service('returnHttp',  ['$q', function($q){
	// Return public API
	return({
		handleError: handleError,
		handleSuccess: handleSuccess
	});
	
	function handleError(response){
		if ( !angular.isObject(response.data) || !response.data.message ) {
			return $q.reject('Ha ocurrido un error desconocido.');
		}
		//console.log('Error:' + response.statusText + '(' + response.status + ') -- ver window.serviceErrorDetalle');
		window.serviceErrorDetalle ='Info Error Service: ' + response.data;
		return $q.reject(response.data.message);
	}
	
	function handleSuccess(response){
		return response.data;
	}

}]);