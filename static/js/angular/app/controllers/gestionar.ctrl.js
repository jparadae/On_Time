appAgenda

appAgenda.controller('GestionarCtrl', ['$scope', '$mdDialog', 'apiAgenda', 'apiTransversal', 'apiContactabilidad', function($scope, $mdDialog, apiAgenda, apiTransversal, apiContactabilidad) {
	
		$scope.form_enviando = false;
		
		apiTransversal.getClientes().then(function(data){
			$scope.clientes = data;
		});
	
		apiAgenda.getCitas().then(function(data){
			$scope.especialidades = data;
		});
	
		apiAgenda.getReservasPendientes().then(function(data){
			$scope.reservas_pendientes = data;
		});
	
		apiAgenda.getReservasHistoricas().then(function(data){
			$scope.reservas_historicas = data;
		});
	
		apiTransversal.getProfesionales().then(function(data){
			$scope.profesionales = data;
		});
	
		$scope.confirmarCitas = function() {
			//console.log('Funcion');
			$scope.form_enviando = true;
			var confirm = $mdDialog.confirm()
				.title('Confirmación de Agenda Dideco')
				.textContent('¿Está seguro que desea enviar una campaña de confirmación de agenda?')
				.ok('Si')
				.cancel('No');
			$mdDialog.show(confirm).then(function() {
				var is_valid = true;
				var count = 0;
				angular.forEach($scope.reservas_pendientes, function(item){
					//console.log(item);
					//console.log('no entra', item.select);
					if(item.select){
						count++;
						//console.log('conteo');
						if(item.contact_campania){
							is_valid = false;
							//console.log(is_valid);
						}
					}
				});
				if(is_valid && count){
					var campania = 0;
					var status = 0;
					var countSend = 0;
	
					apiContactabilidad.createCampania(86) //2 == Confirmación de Citas 
					.then(function(data){
						campania = data.data.id_campania;
						console.log("campania");
						console.log(campania);
						status = 1;
						
						angular.forEach($scope.reservas_pendientes, function(item){
							console.log("item");
							console.log(item);
							if(item.select){

							apiContactabilidad.sendCita( campania, item.id, item.paciente.rut, item.paciente.nombre, item.paciente.telefono, item.cita.especialidad, item.cita.fecha_citacion, item.cita.hora_citacion, item.cita.profesional.rut, item.cita.profesional.nombre, item.cita.cliente.nombre )
								.then(function(data){
									console.log("data");
									console.log(data);
									console.log(campania, item.id, item.paciente.rut, item.paciente.nombre, item.paciente.telefono, item.cita.especialidad, item.cita.fecha_citacion, item.cita.hora_citacion, item.cita.profesional.rut, item.cita.profesional.nombre, item.cita.cliente.nombre);
									countSend++;
	
									apiAgenda.setCampania(item.id, campania, status).then(function(data){
										console.log("llama a setCampania");
										//console.log("item.id");
										//console.log(item.id);
										apiAgenda.getReservasPendientes().then(function(data){
											$scope.reservas_pendientes = data;
										});
										apiAgenda.getReservasHistoricas().then(function(data){
											$scope.reservas_historicas = data;
										});
									});
	
									if(count == countSend){
										$scope.form_enviando = false;
										Materialize.toast('Confirmación de Cita enviada correctamente', 4000);
									}								
								}, function(data){
									Materialize.toast(data, 4000);
								});
							}
						});
					}, function(data){
						$scope.form_enviando = false;
						Materialize.toast(data, 4000);
					});
				}else{
					$scope.form_enviando = false;
					Materialize.toast('Favor seleccionar solo las citas pendientes', 4000);		
				}
	
			}, function() {
				$scope.form_enviando = false;
				//console.log('NO estoy seguro');
			});
		};
	
		$scope.anularCitas = function() {
			$scope.form_enviando = true;
			var confirm = $mdDialog.confirm()
				.title('Anular Hora en Agenda')
				.textContent('¿Está seguro que desea Anular la agenda?')
				.ok('Si')
				.cancel('No');
			$mdDialog.show(confirm).then(function() {
				var is_valid = true;
				//console.log(is_valid);
				var count = 0;
				angular.forEach($scope.reservas_pendientes, function(item){
					if(item.select){
						count++;
						if(item.contact_campania){
							is_valid = false;
						}
					}
				});
				if(is_valid && count){
					var campania = 0;
					var status = 0;
					var countCancel = 0;
	
					apiContactabilidad.createCampania(102) //2 == Confirmación de Citas 102
					.then(function(data){
						campania = data.data.id_campania;
						status = 2;
								   angular.forEach($scope.reservas_pendientes, function(item){
							if(item.select){
	
								apiContactabilidad.cancelCita( campania, item.id, item.paciente.rut, item.paciente.nombre, item.paciente.telefono, item.cita.especialidad, item.cita.fecha_citacion, item.cita.hora_citacion, item.cita.profesional.rut, item.cita.profesional.nombre, item.cita.cliente.nombre )
								.then(function(data){
									countCancel++;
	
									apiAgenda.setCampania(item.id, campania, status).then(function(data){
										apiAgenda.getReservasPendientes().then(function(data){
											$scope.reservas_pendientes = data;
										});
										apiAgenda.getReservasHistoricas().then(function(data){
											$scope.reservas_historicas = data;
										});
									});
	
									if(count == countCancel){
										$scope.form_enviando = false;
										Materialize.toast('Anulación de Cita enviada correctamente', 4000);
									}								
								}, function(data){
									Materialize.toast(data, 4000);
								});
							}
						});
					}, function(data){
						$scope.form_enviando = false;
						Materialize.toast(data, 4000);
					});
				}else{
					$scope.form_enviando = false;
					Materialize.toast('Favor seleccionar solo las citas pendientes', 4000);		
				}
	
			}, function() {
				$scope.form_enviando = false;
				//console.log('NO estoy seguro');
			});
	
		};

		var selec = 0;
		$('body').on( 'click', '.checkall', function(){
			angular.forEach($scope.reservas_pendientes, function(item){
                if(item.contact_campania == null){
                    if(item.select){
                        item.select = false;
                    }else{
                        item.select = true;
                    }
                    var elemento = $('.check');
                    angular.forEach(elemento, function(data){
                        console.log(data);
        
                        if ( selec == 1){
                            $(data).prop('checked', false);
                        }
                        else{
                            $(data).prop('checked', true );
                        }
                    });
                    if(selec == 1){
                        selec = 0;
                    }else{
                        selec = 1;
                    }
                }
			});
			
		});
	
		$(document).ready(function(){
			
			//console.log(pickerFecha);
	
			console.log();
		});
}]);