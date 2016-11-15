$(function() {
    $('#test1').click(function(e){
        console.log("test1");
        $("textarea").val("ลูกบอลถูกปาขึ้นในทิศทำมุมเงย 30 องศา  ด้วยความเร็ว 30 เมตร/วินาที  จงหาความเร็วสุดท้าย ลูกบอลจึงขึ้นได้สูง 10 เมตร ");
    });
    $('#test2').click(function(e){
        $("textarea").val(" วัตถุก้อนหนึ่งถูกยิงขึ้นในทิศทำมุม 30 องศา   กับแนวระดับด้วยความเร็วต้น 80 เมตร/วินาที    จะกินเวลานานเท่าไรวัตถุนั้นจึงตกถึงพื้น");

    });
    $('#test3').click(function(e){
        $("textarea").val("วัตถุกำลังเคลื่อนที่ด้วยความเร็วต้น 4 เมตร/วินาที ไปทางทิศตะวันตก จากนั้นได้รับความเร่ง 5 เมตร/วินาทียกกำลังสอง ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วปลายของวัตถุ");
    });

    $("textarea").keydown(function(e) {
        // Enter was pressed without shift key
        $("ul.recomm").find($('.active'))
        if (e.keyCode == 13 && !e.shiftKey) {
            e.preventDefault();
        }
        else if(e.keyCode==38 && !e.shiftKey){
            e.preventDefault();
        }
        else if(e.keyCode==40 && !e.shiftKey){
            e.preventDefault();

        }
        
    });
    // $("button#answers").click(function (){
    //     $.ajax({
    //         type: "GET",
    //         url: $SCRIPT_ROOT + "/test/",
    //         contentType: "application/json; charset=utf-8",
    //         data: {
    //             problem: $("textarea").val()
    //         },
    //         success: function(data) {
    //           preword=data.value
    //           console.log(data.value)
    //           $('.preword').text(data.value)
    //         }
    //     });
    // });
    // function findWord(newword) {

    //     $.ajax({
    //         type: "GET",
    //         url: $SCRIPT_ROOT + "/preword/",
    //         contentType: "application/json; charset=utf-8",
    //         data: {
    //             word: newword
    //         },
    //         success: function(data) {
    //           preword=data.value
    //           console.log(data.value)
    //           $('.preword').text(data.value)
    //         }
    //     });
    //     return preword

    // }
});