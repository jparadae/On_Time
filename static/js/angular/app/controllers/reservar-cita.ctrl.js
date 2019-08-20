var appAgenda = angular.module('appAgenda', []);

appAgenda.controller('ReservarCtrl', ['$scope', 'apiAgenda', 'apiTransversal', function($scope, apiAgenda, apiTransversal) {
	
	apiTransversal.getClientes().then(function(data){
		$scope.clientes = data;
	});

	apiAgenda.getCitasDisponibles().then(function(data){
		$scope.citas = data;
	});

	apiTransversal.getProfesionales().then(function(data){
		$scope.profesionales = data;
	});

	$scope.selectHora = function($event){
		var cita = $($event.currentTarget).attr('data-cita');
		$scope.form.cita = cita;
	}

	$scope.resetHora = function(){
		$scope.form.cita = '';
		$('input[name=hora_select]').removeAttr('checked');
	}

	$scope.getDatosPaciente = function(){
		apiTransversal.getPacientePorRut($scope.form.rut).then(function(data){
			var items = ['nombre', 'apellidos', 'email', 'telefono', 'direccion'];
			angular.forEach(items, function(item){
				var value = data[item];
				if(value){
					if(item == 'telefono'){
						value = parseInt(value);
					}
					$scope.form[item] = value;
					$('input[name=' + item + ']').siblings('label').addClass('active')
												 .siblings('i').addClass('active');
				}

			});
			
		}, function(data){
			var items = ['nombre', 'apellidos', 'email', 'telefono', 'direccion'];
			angular.forEach(items, function(item){
				$scope.form[item] = '';
				$('input[name=' + item + ']').siblings('label').removeClass('active')
											 .siblings('i').removeClass('active');
			});			
		});
	}

	$scope.resetForm = function(){
		$('[data-step=2]').trigger('click')
						  .parent().addClass('disabled');
		$('[data-step=3]').trigger('click')
						  .parent().addClass('disabled');
		
		$scope.form = {}; //Reset form
	}

	$scope.submitReserva = function(step){ //aqui llamo a las citas disponibles para reservar
		if(step == 3){
			var result = [];
			apiAgenda.addReserva($scope.form)
				.then(function(data){
					$scope.resetForm();
					apiAgenda.getCitasDisponibles().then(function(data){
						$scope.citas = data;
					});
					Materialize.toast(data.status, 4000);
				}, function(data){
					Materialize.toast(data, 4000);
				});

		}else{
			var next_step = step + 1;
			var $next_header = $('[data-step=' + next_step + ']');

			$next_header.parent().removeClass('disabled');
			if(!$next_header.hasClass('active')){
				$next_header.trigger('click');
			}

			setTimeout(function() {
				if(step == 1){
					//pickerFecha.show();	
					$('body').scrollTop(300)
				}else{
					$('body').scrollTop(400);
					$('input[name="rut"]').focus();
				}
			}, 300);
		}
	}


    $(document).ready(function(){
		//console.log('here');
		//alert(moment().format("YYYY,M,DD"));
		//var fecha = moment().format("YY-MM-DD");

		$scope.fecha = moment().format("YYYY,M,DD");


	});


}]);
