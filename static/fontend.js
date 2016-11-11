$(function() {
    $('#test1').click(function(e){
        console.log("test1");
        $("textarea").val("วัตถุกำลังเคลื่อนที่ด้วยความเร็ว 40 m/s ไปทางทิศตะวันตก  จากนั้นได้รับความเร่ง 10 เมตรต่อวินาทียกกำลังสอง ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วของวัตถุ");
    });
    $('#test2').click(function(e){
        $("textarea").val("วัตถุมวล 10 kg เคลื่อนที่เป็นเส้นตรงมีความเร็วต้น 20 m/s มีความเร่ง 5 เมตรต่อวินาทียกกำลังสอง ถ้าให้เคลื่อนที่เป็นเวลา 20 s จะมีความเร็วเท่าไร");

    });
    $('#test3').click(function(e){
        $("textarea").val("วัตถุกำลังเคลื่อนที่ด้วยความเร็ว 4 เมตร/วินาที ไปทางทิศตะวันตก จากนั้นได้รับความเร่ง 5 เมตร/วินาทียกกำลังสอง ไปทางทิศตะวันออกเป็นเวลา 5 วินาที จงหาความเร็วของวัตถุ");
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
    $("button#answers").click(function (){
        $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + "/test/",
            contentType: "application/json; charset=utf-8",
            data: {
                problem: $("textarea").val()
            },
            success: function(data) {
              preword=data.value
              console.log(data.value)
              $('.preword').text(data.value)
            }
        });
    });
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