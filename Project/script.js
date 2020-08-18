// Code goes here

var app = angular.module('app', []);

app.directive('sortable', function($timeout) {
  return function(scope, element, attributes) {
    element.sortable({
      stop: function(event, ui) {
        scope.$apply(function() {
          scope.syncOrder(element.sortable('toArray'));
        });
      }
    });
  };
});

app.controller('Ctrl1', function($scope) {

  $scope.listData = ["doremon", "wonder women", "anks", "crazy hair"];

  $scope.objects = [];
  for (var count = 0; count < $scope.listData.length; count++) {
    $scope.objects.push({
      id: count,
      sortOrder: count,
      message: $scope.listData[count]
    });
  }

  $scope.syncOrder = function(elemPositions) {
    $scope.objects.forEach(function(obj) {
      elemPositions.forEach(function(elemId, index) {
        var id = parseInt(elemId.replace(/elem-/, ''));
        if (id === obj.id) {
          obj.sortOrder = index;
        }
      });
    });
    //alert();
    //$scope.listData.remove($scope.objects.id);
    // $scope.listData.add($scope.objects.sortOrder);
  };

  $scope.addItem = function() {
    if ($scope.newItem.length > 0) {
      $scope.objects.push({
        id: (($scope.objects[$scope.objects.length - 1].id) + 1),
        sortOrder: $scope.listData.length,
        message: $scope.newItem
      });
      $scope.listData.push($scope.newItem);
      $scope.newItem = "";
    }
  };

  $scope.deleteItem = function(idx) {
    $scope.listData.splice(idx, 1);
    $scope.objects.splice(idx, 1);
  };

  $scope.updateValue = function(idx, data) {
    $scope.listData[idx] = data;
    $scope.objects[idx].message = data;
  };

  $scope.doSubmit = function() {
    $scope.formOutput = alert($scope.listData);
  };
})


//$(document).ready(function(){});