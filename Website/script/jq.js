/**
 * Created by Drew Langley on 9/21/2016.
 */

$(document).ready(function()
{
    $ogBGhoversColor = $(".hover, .hover2, .hover3, .hover4").css("background-color");


    $(".hover").mouseover(function()
    {
       $(this).css("background-color", "rgba(0, 0, 255, 0.2)");
    });

    $(".hover2").mouseover(function()
    {
        $(this).css("background-color", "rgba(255, 0, 0, 0.2)");
    });

    $(".hover3").mouseover(function()
    {
        $(this).css("background-color", "rgba(0, 255, 0, 0.2)");
    });

    $(".hover4").mouseover(function()
    {
        $(this).css("background-color", "rgba(255, 255, 0, 0.2)");
    });

    $(".hover, .hover2, .hover3, .hover4").mouseout(function()
    {
       $(this).css("background-color", $ogBGhoversColor);
    });

});