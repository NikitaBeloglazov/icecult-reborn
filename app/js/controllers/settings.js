/* Copyright (c) 2015 Lars Kreisz (under MIT) */
/* Copyright (c) 2023 Nikita Beloglazov */
/* License: Mozilla Public License 2.0 */

'use strict';

EiskaltApp.controller('SettingsCtrl', function ($scope, $timeout, $modal, settings, EiskaltRPC) {
    $scope.settings = settings.settings

    $scope.reset = function() {
        angular.forEach($scope.settings, function (setting) {
            EiskaltRPC.SettingsGetSet(setting.key).success(function(value) {
                if (setting.type === 'number') {
                    value = parseInt(value);
                }
                setting.value = value;
            });
        });
        EiskaltRPC.ListShare().success(function(shares) {
            $scope.shares = shares;
        });
    };
    $scope.reset();

    $scope.save = function() {
        angular.forEach($scope.settings, function (setting) {
            EiskaltRPC.SettingsGetSet(setting.key, setting.value).success(function(success) {
                if (success) {
                    setting.success = true;
                    $timeout(function() {
                        delete setting.success;
                    }, 2000)
                } else {
                    setting.error = true;
                }
            });
        });
    };
});