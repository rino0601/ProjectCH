/**
 * Created by lemonApple on 2/28/15.
 */
//(function () {
//    'use strict';
//});
var app = angular.module('CHApp', ['ngMaterial'])
        .config(function ($interpolateProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
        })
        .controller('AppCtrl', [
            '$scope',
            '$mdSidenav',
            function ($scope, $mdSidenav) {
                //define function.
                $scope.toggleSidenav = function (menuId) {
                    $mdSidenav(menuId).toggle();
                };

            }
        ])

    ;
