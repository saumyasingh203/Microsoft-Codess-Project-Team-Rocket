// let scores = [
//     { name: "Player 1", score: 300 },
//     { name: "Player 2", score: 370 },
//     { name: "Player 3", score: 500 },
//     { name: "Player 4", score: 430 },
//     { name: "Player 5", score: 340 },
// ];

$.getJSON("/scores").then((data) => {
    scores = data;
    console.log(scores, scores.length)
    //   console.log(scores);
  });
  $.getJSON("/get-user").then((data) => {
    //   console.log(data["email"]);
    currentUser = data;
    //   console.log(data);
    //   console.log(currentUser);
    score = data["score"];
    //   console.log(parseInt(score));
    //   newscore = parseInt(score) + 400;
    //   console.log(newscore);
    //   console.log(currentUser);
  
    ////testing if code works
    //   $.post("update-score", {
    //     name: currentUser.name + "a",
    //     email: currentUser.email,
    //     score: newscore,
    //     message: currentUser.message,
    //   });
    ////success
  });

function checkscore() {
    let j = 0;
    for (let i = 3; j <= 12; i = i + 3) {
        console.log(scores[j])
        document.querySelectorAll(".leader-table td")[i].innerHTML = j+1;
        document.querySelectorAll(".leader-table td")[i+1].innerHTML = scores[j].name;
        document.querySelectorAll(".leader-table td")[i + 2].innerHTML = scores[j].score;
        j = j + 1;
    }
}



function level_click(thisid) {
    for (var i = 1; i <= 4; i++) {
        document.querySelector("#level-" + i).classList.remove("pressed");
    }
    document.querySelector("#level-" + thisid).classList.add("pressed");

    console.log('/level' + thisid);

    $.getJSON('/level' + thisid, {}, {});

}


function startwith(thisid)
{
    document.querySelector("#s1").classList.remove("pressedStart");
    document.querySelector("#s2").classList.remove("pressedStart");
    document.querySelector("#s" + thisid).classList.add("pressedStart");

    if (thisid == 1) {
        $.getJSON('/startAI', {},
           function (data) {
            for (var i = 1; i <= 9; i++) {
                cell = document.getElementById(String(i));
                cell.innerHTML = data.board[i];
            }
          });
                  
    }
    else {
        $.getJSON('/startHuman', {},
                   function (data) {
            for (var i = 1; i <= 9; i++) {
                cell = document.getElementById(String(i));
                cell.innerHTML = data.board[i];
            }
          });
    }


}



function reply_click(thisid) {
    console.log(thisid);
    // cell = document.getElementById(String(thisid));
    // cell.innerHTML = "O";

    $.getJSON('/number' + thisid, {},
        function (data) {
            for (var i = 1; i <= 9; i++) {
                cell = document.getElementById(String(i));
                cell.innerHTML = data.result[i];
            }
            if(data.status ==1 ) {
                //player wins
                let currentScore = parseInt(score) + 5;
                //post request to increase the score by 5
                $.post("update-score", {
                    name: currentUser.name,
                    email: currentUser.email,
                    score: currentScore,
                    message: currentUser.message,
                });
                document.getElementById("message").innerHTML = "Wuhoo, You Won :)";
            }
            if(data.status ==0 ) {
                //tie
                document.getElementById("message").innerHTML = "It's a Tie :|";
            }
            if(data.status == -1 ) {
                //computer wins
                let currentScore = parseInt(score) - 1;
                $.post("update-score", {
                    name: currentUser.name,
                    email: currentUser.email,
                    score: currentScore,
                    message: currentUser.message,
                });
                document.getElementById("message").innerHTML = "Oops, You Lost :(";
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
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
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
