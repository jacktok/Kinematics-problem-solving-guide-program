var app = angular.module('myapp', []);
var active
var len = 0,
    buflen
app.controller('controll', ['$scope', '$timeout', '$http', function($scope, $timeout, $http) {
    $scope.data = ['a']
    $scope.recommendShow=false;
    $scope.$watch('wordrecommand', function() {
        console.log($scope.wordrecommand)
    })
    $scope.test=function(){
    	console.log("dada")
    }
    $scope.recomm = function(e) {
        active = $('ul.recomm').find($('.active')).index()
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


        } else if (e.keyCode != 37 && e.keyCode != 39 && $("#check").val().replace(/" "/g,'')!='') {
            $('.recomm li').removeClass('active')

            $.ajax({
                type: "GET",
                url: $SCRIPT_ROOT + "/preword/",
                contentType: "application/json; charset=utf-8",
                data: {
                    word: $("#check").val()
                },
                success: function(data) {
                    console.log(data.value)
                    $scope.wordrecommand = data.value;
                }
            });
            $scope.test('s')

        }


        if ($scope.wordrecommand !== 'undefined') {
            $('ul.recomm li:eq(0)').addClass('active')
        }
    }
    $scope.getRecommend=function(){


    	$.ajax({
                type: "GET",
                url: $SCRIPT_ROOT + "/recommend/",
                contentType: "application/json; charset=utf-8",
                data: {
                    problem: $("#check").val()
                },
                success: function(data) {
                    console.log(data.value)
                    $scope.recommend = data.value;
                }
            });


    }
    




}])

