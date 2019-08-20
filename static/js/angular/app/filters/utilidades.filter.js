appAgenda.filter('filterCustom', ['$parse', function($parse) {
	return function(input, key, model, showAll) {
		var result = [];
		angular.forEach(input, function(item) {
			if(showAll && !model){
				result.push(item)				
			}else{
				var parseKey = $parse(key);
				if (parseKey(item) == model) {
					result.push(item)
				}				
			}
		})
		return result;
	}
}]);

appAgenda.filter('filterRange', ['$parse', function($parse) {
	return function(data, inicio, fin) {
		var array = [];
		angular.forEach(data, function(data){
			if(inicio && fin){
				if(data.cita.fecha_citacion >= inicio && data.cita.fecha_citacion <= fin){
					array.push(data)
				}
			}else{
				array.push(data)
			}
		})
		return array;
	}
}]);

appAgenda.filter('filterEstados', ['$parse', function($parse) {
	return function(data, estado) {
		var array = [];
		angular.forEach(data, function(data){
			if(estado){
				if(data.contact_status == estado){
					array.push(data)
				}
			}else{
				array.push(data)
			}
		})
		return array;
	}
}]);

appAgenda.filter('groupBy', ['$filter', function($filter){
    return function(list, group_by) {

		var filtered = [];
		var prev_item = null;
		var group_changed = false;
		var new_field = group_by + '_CHANGED';

		list = $filter('orderBy')(list, group_by);

		angular.forEach(list, function(item, i) {

			group_changed = false;
			if (prev_item !== null) {
				if (prev_item[group_by] !== item[group_by]) {
					group_changed = true;
				}
			} else {
				group_changed = true;
			}

			if (group_changed) {
				item[new_field] = true;
			} else {
				item[new_field] = false;
			}

			filtered.push(item);
			prev_item = item;

		});
		
		return filtered;
	};
}])