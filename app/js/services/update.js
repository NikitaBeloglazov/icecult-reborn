/* Copyright (c) 2015 Lars Kreisz (under MIT) */
/* Copyright (c) 2023 Nikita Beloglazov */
/* License: Mozilla Public License 2.0 */

'use strict';

angular.module('UpdateCheck', []).factory('UpdateCheck', function($http, settings) {

    var api = settings.updateUrl + '?callback=JSON_CALLBACK';

    var find = function(arr, name) {
        var filtered = arr.filter(function(e) { return e.tag_name === name});
        return filtered.length ? filtered[0] : null
    }

    var newVersion = function(currentVersion) {
        var promise = $http.jsonp(api);
        promise.success = function(fn) {
            promise.then(function(response) {
                if (response.status !== 200) {
                    fn(null);
                }
                var versions = response.data.data;
                var latest = versions[0];
                var current = find(versions, currentVersion.client);
                fn(new Date(current.published_at) < new Date(latest.published_at) ? latest : null);
            });
        }
        return promise;
    }

    return {
        getNewerVersion: newVersion
    }
});
