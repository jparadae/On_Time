var appAgenda = angular.module('appAgenda', []);

appAgenda.controller('CargarCitasCtrl', ['$scope', 'apiAgenda', 'apiTransversal', function($scope, apiAgenda, apiTransversal) {
	
	apiTransversal.getClientes().then(function(data){
		$scope.clientes = data;
	});

	apiTransversal.getProfesionales().then(function(data){
		$scope.profesionales = data;
	});

	$scope.horas = [15, 16, 17]; //se modifica para dideco
//se arregla lapsus c/15 min y 20 para dideco
	$scope.generateCitas = function(){
		$scope.citas = [];
		if($scope.form.horario.desde && $scope.form.horario.hasta && $scope.form.intervalo){
			for (var i = parseInt($scope.form.horario.desde); i <= parseInt($scope.form.horario.hasta); i++) {
				$scope.citas.push({'hora': i, 'minuto': '00', 'cupo': true, 'sobrecupo1': false, 'sobrecupo2': false})
				if($scope.form.horario.hasta > i){
					if($scope.form.intervalo == 15 && (i < $scope.form.horario.hasta)){
						$scope.citas.push({'hora': i, 'minuto': '15', 'cupo': true, 'sobrecupo1': false, 'sobrecupo2': false});
						$scope.citas.push({'hora': i, 'minuto': '20', 'cupo': true, 'sobrecupo1': false, 'sobrecupo2': false});
						$scope.citas.push({'hora': i, 'minuto': '45', 'cupo': true, 'sobrecupo1': false, 'sobrecupo2': false});
					}else if($scope.form.intervalo == 20 && (i < $scope.form.horario.hasta)){
						$scope.citas.push({'hora': i, 'minuto': '20', 'cupo': true, 'sobrecupo1': false, 'sobrecupo2': false});
					}
				}
			}			
		}
	}

	$scope.resetForm = function(){		
		$scope.citas = {}; //Reset form
		$scope.form = {}; //Reset form
	}

	$scope.submitCarga = function(){
		var countCarga = {'correctas': 0, 'fallidas': 0};
		angular.forEach($scope.citas, function(item){
			var cupos = (item.cupo ? 1 : 0) + (item.sobrecupo1 ? 1 : 0) + (item.sobrecupo2 ? 1 : 0);
			if(cupos){
				var dataForm = {'cliente': $scope.form.cliente, 'profesional': $scope.form.profesional, 'especialidad': $scope.form.especialidad, 'fecha': $scope.form.fecha, 'hora': item.hora + ':' + item.minuto, 'cupos': cupos};
				apiAgenda.addCita(dataForm)
					.then(function(data){
						countCarga.correctas += 1;
					}, function(data){
						countCarga.fallidas += 1;
					});
			}
		});

		setTimeout(function() {
			//console.log('Cargas Correctas: ' + countCarga.correctas);
			//console.log('Cargas Fallidas: ' + countCarga.fallidas);
			if(countCarga.fallidas){
				Materialize.toast('Algunas citas de agenda no se pudieron cargar', 4000);
			}else if(countCarga.correctas){
				Materialize.toast('Citas de agenda cargadas correctamente', 4000);
			}else{
				Materialize.toast('No se cargó ninguna Cita', 4000);			
			}
		}, 1000);
		$scope.resetForm();
	}

}]);
