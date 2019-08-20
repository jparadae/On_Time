var appAgenda = angular.module('appAgenda', ['ngMaterial']);


appAgenda.directive('fluqueDatePicker', function (){
    var picker = {
        restrict: 'AE',
        $scope: {},
        templateUrl:'/static/js/angular/app/templates/datePicker.html/?v=2',
        link: true
    };

    return picker;
});
