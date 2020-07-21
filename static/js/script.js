
function level_click(thisid)
{
    for (var i = 1; i <=4 ; i++) {
        document.querySelector("#level-" + i).classList.remove("pressed");
    }
    document.querySelector("#level-" + thisid).classList.add("pressed");

    console.log('/level' + thisid);
    $.getJSON('/level' + thisid, {},{});
    
}


function startwith(thisid)
{
    document.querySelector("#s1").classList.remove("pressedStart");
    document.querySelector("#s2").classList.remove("pressedStart");
    document.querySelector("#s" + thisid).classList.add("pressedStart");
}



function reply_click(thisid)
{
    console.log(thisid);
    // cell = document.getElementById(String(thisid));
    // cell.innerHTML = "O";

    $.getJSON('/number' + thisid, {},
    function (data)
    {
        for (var i = 1; i <= 9; i++) {
            cell = document.getElementById(String(i));
            cell.innerHTML = data.result[i];
        }

        console.log(data.hasWon);
        console.log(data.winBoard);
        if (data.hasWon == 1) {
            for (var i = 0; i < 3; i++)
                document.getElementById(String(data.winBoard[i])).style.color = "red";
        }
    });
    
}



//********************************* THIS IS FOR MAIN.HTML ******************************************//

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("play-button");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


//********************************* WATER FORM *******************************************//


$('document').ready(function () {
    $('input[type="text"], input[type="email"], textarea').focus(function () {
        var background = $(this).attr('id');
        $('#' + background + '-form').addClass('formgroup-active');
        $('#' + background + '-form').removeClass('formgroup-error');
    });
    $('input[type="text"], input[type="email"], textarea').blur(function () {
        var background = $(this).attr('id');
        $('#' + background + '-form').removeClass('formgroup-active');
    });

    function errorfield(field) {
        $(field).addClass('formgroup-error');
        console.log(field);
    }

    $("#waterform").submit(function () {
        var stopsubmit = false;

        if ($('#name').val() == "") {
            errorfield('#name-form');
            stopsubmit = true;
        }
        if ($('#email').val() == "") {
            errorfield('#email-form');
            stopsubmit = true;
        }
        if (stopsubmit) return false;
    });

});