function filterGrilla(filtro){
	var tableBody = $('table tbody');
	var tableRowsClass = $('table tbody tr');
	$('.search-sf').remove();
	tableRowsClass.each( function(i, val) {

		//Lower text for case insensitive
		var rowText = $(val).text().toLowerCase();
		var inputText = $(filtro).val().toLowerCase();
		if(inputText != ''){
			$('.search-query-sf').remove();
			//tableBody.prepend('<tr class="search-query-sf"><td colspan="6"><strong>Filtrando por: "' + $(filtro).val() + '"</strong></td></tr>');
		}else{
			$('.search-query-sf').remove();
		}

		if( rowText.indexOf( inputText ) == -1 ){
			//hide rows
			tableRowsClass.eq(i).hide();
		}else{
			$('.search-sf').remove();
			tableRowsClass.eq(i).show();
		}
	});
	//all tr elements are hidden
	if(tableRowsClass.children(':visible').length == 0){
		tableBody.append('<tr class="search-sf"><td class="text-muted" colspan="6">No hay registros.</td></tr>');
	}

	countRegistrosGrilla(false);
};

function countRegistrosGrilla(modal){
	var contentGrilla = (modal) ? '.grilla-modal' : '.grilla';
	var count = $(contentGrilla + ' table tbody tr:visible').length;
	var plural = '';
	var elemento = $('.info-count').find('span');

	if(count > 1){ plural = 's'; }
	elemento.text(count + ' registro' + plural + ' encontrado' + plural + '.');
}

function exportGrilla(){
	var html = $('.grilla:visible').html();
	while (html.indexOf('á') != -1) html = html.replace('á', '&aacute;');
	while (html.indexOf('é') != -1) html = html.replace('é', '&eacute;');
	while (html.indexOf('í') != -1) html = html.replace('í', '&iacute;');
	while (html.indexOf('ó') != -1) html = html.replace('ó', '&oacute;');
	while (html.indexOf('ú') != -1) html = html.replace('ú', '&uacute;');
	while (html.indexOf('ñ') != -1) html = html.replace('ñ', '&ntilde;');
	while (html.indexOf('Ñ') != -1) html = html.replace('Ñ', '&Ntilde;');
	while (html.indexOf('º') != -1) html = html.replace('º', '&ordm;');
	window.open('data:application/vnd.ms-excel,' + encodeURIComponent(html))
}

var formatNumber = {
	separador: ".", // separador para los miles
	sepDecimal: ',', // separador para los decimales
	formatear:function (num){
		num +='';
		var splitStr = num.split('.');
		var splitLeft = splitStr[0];
		var splitRight = splitStr.length > 1 ? this.sepDecimal + splitStr[1] : '';
		var regx = /(\d+)(\d{3})/;
		while (regx.test(splitLeft)) {
			splitLeft = splitLeft.replace(regx, '$1' + this.separador + '$2');
		}
		return this.simbol + splitLeft  +splitRight;
	},
	new:function(num, simbol){
		this.simbol = simbol ||'';
		return this.formatear(num);
	}
}

function validarEmail( email ) {
    expr = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( !expr.test(email) ){
        Materialize.toast("Error: La dirección de correo " + email + " es incorrecta.", 4000);
        return false;
    }

    return true;
}

function replaceAll(find, replace, str) {
	return str.split(find).join(replace);
}

function disabledBtnFormOnSubmit(){
	$('[type="submit"]:not(.no-loading)').on('click', function(){
		showCargando($(this), '<br/>');
	});
}

function showCargando($element, salto = ''){
	$element.css('display', 'none');
	$element.parent().append(salto + '<span>Favor espere... </span><div class="preloader-wrapper small active"><div class="spinner-layer spinner-blue-only"><div class="circle-clipper left"><div class="circle"></div></div><div class="gap-patch"><div class="circle"></div></div><div class="circle-clipper right"><div class="circle"></div></div></div></div>');
}

function showNotificacion(titulo, contenido, icono){
	if (!("Notification" in window)) { 
		console.log("Este navegador no soporta las notificaciones de escritorio.");
	}else if (Notification.permission === "granted" ) { 
		var options = { 
			body : contenido,
			icon : icono,
			dir  : "ltr"
		};
		var notification = new Notification(titulo, options);
	}else if (Notification.permission !== 'denied') { 
		Notification.requestPermission(function (permission){ 
			if (!('permission' in Notification)) { 
				Notification.permission = permission;
			} 

			if (permission === "granted" ) { 
				var options = { 
					body : contenido,
					icon : icono,
					dir  : "ltr" 
				}; 
				var notification = new Notification(titulo, options);
			} 
		});
	}
}

function showMenu(init){
	var $menu = $('#nav-mobile');
	var $panel = $('#section');
	var $footer = $('.footer div');
	var $btnBarmenu = $('.btn-show-barmenu');

	if( (init && localStorage.getItem('showMenu') == 'false') || (!init && $menu.hasClass('s1')) ){
		if(!init){
			$menu.css('transition', '0.3s');
		}
		$menu.addClass('s0').removeClass('s1');
		$panel.addClass('m12').removeClass('m11').removeClass('offset-m1');
		$footer.addClass('m12').removeClass('m11').removeClass('offset-m1');

		localStorage.setItem('showMenu', false);
		$btnBarmenu.addClass('hide-menu');
	}else{
		$menu.css('transition', '').addClass('s1').removeClass('s0');
		$panel.addClass('m11').addClass('offset-m1').removeClass('m12');
		$footer.addClass('m11').addClass('offset-m1').removeClass('m12');

		localStorage.setItem('showMenu', true);
		$btnBarmenu.removeClass('hide-menu');
	}
}

function validationForm(){
	var validado = true;
	var $form = $('form');

	var elementos = ['input', 'select', 'textarea'];

	$.each(elementos, function(i, val){
		$form.find(val + '.requerido').each(function(i){
			var label = $(this).attr('data-label');
			var val = $(this).val();

			if(!val || val == 0){
				Materialize.toast("El campo '" + label + "' es requerido.", 4000);
				validado = false;
			}
		});
	});

	return validado;
}

function getCoordenadas($form){
	$coordenadas = $('input[name="coordenadas"]');

	if($coordenadas.val()){
		$form.submit(); //Envia el formulario
	}else{
		navigator.geolocation.getCurrentPosition(function(objPosition){
			var lon = objPosition.coords.longitude;
			var lat = objPosition.coords.latitude;

			//console.log('Coordenadas: ' + lat + ',' + lon);
			$coordenadas.val(lat + ',' + lon);

			$form.submit(); //Envia el formulario

		}, function(objPositionError){
			switch (objPositionError.code){
				case objPositionError.PERMISSION_DENIED:
					//Materialize.toast('No se ha permitido el acceso a la georeferencia del usuario.', 4000);
					//console.log(objPositionError);
				break;
				case objPositionError.POSITION_UNAVAILABLE:
					Materialize.toast('No se ha podido acceder a la información de su georeferencia', 4000);
					//console.log('No se ha podido acceder a la información de su georeferencia.');
				break;
				case objPositionError.TIMEOUT:
					Materialize.toast('El servicio ha tardado demasiado tiempo en responder.', 4000);
				break;
				default:
					Materialize.toast('Error desconocido.', 4000);
			}

			//showPanelCargando(false);
			$form.submit(); //Envia el formulario

		}, {
			maximumAge: 75000,
			timeout: 15000
		});
	}
};