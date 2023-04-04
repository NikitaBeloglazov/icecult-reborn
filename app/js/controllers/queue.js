/* Copyright (c) 2015 Lars Kreisz (under MIT) */
/* Copyright (c) 2023 Nikita Beloglazov */
/* License: Mozilla Public License 2.0 */


'use strict';

EiskaltApp.controller('QueueCtrl', function ($scope, $interval, settings, EiskaltRPC) {
    $scope.queue = []
    $scope.refreshQueue = function () {
        EiskaltRPC.ListQueue().success(function(queue) {
            $scope.queue = queue;
        });
    };
    $scope.refreshQueue();
    var refreshQueueTimer = $interval($scope.refreshQueue, settings.refresh.queues);
    $scope.$on("$destroy", function(event) {
        $interval.cancel(refreshQueueTimer);
    });
});

EiskaltApp.controller('QueueItemCtrl', function ($scope, EiskaltRPC) {
    $scope.collapsed = false;

    $scope.changePrio = function (direction) {
        EiskaltRPC.SetPriorityQueueItem(
            $scope.item.Target,
            $scope.item.PriorityOrder + direction
        ).success($scope.refreshQueue);
    };
    $scope.abort = function () {
        EiskaltRPC.RemoveQueueItem($scope.item.Target).success($scope.refreshQueue);
    };
});
