

appAgenda.controller('MisCitasCtrl', ['$scope', '$mdDialog', 'apiAgenda', function($scope, $mdDialog, apiAgenda) {
	
	$scope.reservas_pendientes = [];
	$scope.reservas_historicas = [];

	$scope.searchReservas = function() {
		var rut = $scope.form.rut

		apiAgenda.getMisReservasPendientes(rut).then(function(data){
			$scope.reservas_pendientes = data;
		}, function(data){
			$scope.reservas_pendientes = [];
		});

		apiAgenda.getMisReservasHistoricas(rut).then(function(data){
			$scope.reservas_historicas = data;
		}, function(data){
			$scope.reservas_historicas = [];
		});
	};

	$scope.anularHora = function(cita) {
		var confirm = $mdDialog.confirm()
			.title('Anular Hora en Agenda')
			.textContent('¿Está seguro que desea anular la hora en Agenda Dideco?')
			.ok('Si')
			.cancel('No');
		$mdDialog.show(confirm).then(function() {
			apiAgenda.cancelReserva(cita)
				.then(function(data){
					
					$scope.searchReservas();

					Materialize.toast(data.status, 4000);
				}, function(data){
					Materialize.toast(data, 4000);
				});
		}, function() {
			console.log('NO estoy seguro');
		});
	};

}]);