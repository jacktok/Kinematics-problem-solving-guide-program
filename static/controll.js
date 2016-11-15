var app = angular.module('myapp', []);
var active
var len = 0,
    buflen
app.controller('controll', ['$scope', '$timeout', '$http', '$templateCache', function($scope, $timeout, $http, $templateCache) {
    $scope.data = ['a']
    $scope.recommendShow = false;
    $scope.answersShow = false;
    $scope.success=true;
    $scope.Error=false;

    if($scope.check==''){
            $scope.wordrecommand=[]
        }
    $scope.test = function() {
        console.log("dada")
    }
    $scope.recomm = function(e) {
        active = $('ul.recomm').find($('.active')).index()
        $('.recomm li').removeClass('active')
        if (e.keyCode == 13 && !e.shiftKey) {
            e.preventDefault();
            console.log($('ul.recomm').text())
            if ($('ul.recomm').text().replace(/ /g, '').replace(/\n/g, '') != '') {
                $('textarea').val($('textarea').val() + $('li.word:eq(' + active + ')').text());
            } else {
                $('textarea').val($('textarea').val() + $('#check').val());
            }
            $('#check').val('');
            $('li.word:eq(' + active + ')').removeClass('active');
            $scope.wordrecommand = []

        } else if (e.keyCode == 38 && !e.shiftKey) {
            e.preventDefault();
            $('li.word:eq(' + active + ')').removeClass('active');
            active -= 1;
            $('li.word:eq(' + active + ')').addClass('active')


        } else if (e.keyCode == 40 && !e.shiftKey) {
            e.preventDefault();
            $('li.word:eq(' + active + ')').removeClass('active');
            active += 1;
            $('li.word:eq(' + active + ')').addClass('active')


        } else if (e.keyCode != 37 && e.keyCode != 39 && $("#check").val().replace(/" "/g, '') != '') {
            $('.recomm li').removeClass('active')
            $http({
                url: $SCRIPT_ROOT + "/preword/",
                method: "GET",
                // header:{"contentType": "application/json; charset=utf-8"},
                params: { word: $scope.check }
            }).
            then(function(respond) {
                $scope.wordrecommand = respond.data.value
            });

            if ($scope.wordrecommand !== 'undefined') {
                $('ul.recomm li:eq(0)').addClass('active')
            } else {
                console.log("gaag")
                $scope.wordrecommand = [];
            }

        }



    }
    $scope.getRecommend = function() {

        $scope.Error=false;
        $scope.success=false;
        $scope.recommendShow = false;
        $scope.answersShow = false;
        console.log($scope.recommend);
        $http({
            url: $SCRIPT_ROOT + "/recommend/",
            method: "GET",
            // header:{"contentType": "application/json; charset=utf-8"},
            params: { problem: $("textarea").val() }
        }).
        then(function(respond) {
            $scope.recommend = respond.data.value
            $scope.formula = respond.data.equation
            $scope.variableFind = respond.data.find
            console.log(respond.data.equation)
            $scope.success=true;
            $scope.recommendShow = true;
            if ($scope.formula.length == 0) {
                $scope.recommendFail = true;
            } else {
                $scope.recommendFail = false;
            }
        },function errorCallback(response) {
             $scope.success=true;
            $scope.Error=true;
        })
    }
    $scope.getSolving = function() {
        $scope.Error=false;
        $scope.isMoreStep=false;
        $scope.success=false;
        $scope.recommendShow = false;
        $scope.answersShow = false;

        $http({
            url: $SCRIPT_ROOT + "/test/",
            method: "GET",
            // header:{"contentType": "application/json; charset=utf-8"},
            params: { problem: $("textarea").val() }
        }).
        then(function(respond) {
            $scope.variableSolving = respond.data.value
                // $scope.formulaSolving=respond.data.equation
            $scope.variableFindSolving = respond.data.find
            $scope.stepSolving = respond.data.step
            console.log(respond.data)
            if ($scope.stepSolving.length==2) {
                $scope.lastStepSolving = respond.data.lastStep;
                console.log($scope.lastStepSolving)
                $scope.isMoreStep=true;
            }
            $scope.success=true;
            $scope.answersShow = true
            if ($scope.stepSolving.length == 0) {            
                $scope.recommendFail = true;
            } else {
                $scope.recommendFail = false;
            }
        },function errorCallback(response) {
             $scope.success=true;
            $scope.Error=true;
        });
        console.log($scope.recommendFail)

    }





}])
