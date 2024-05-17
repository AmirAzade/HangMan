const user_name = JSON.parse(document.getElementById('user_name').textContent);

const elemWidth = document.getElementById("Abutton").offsetWidth;
document.getElementById("Abutton").style.height = elemWidth;
document.getElementById("Bbutton").style.height = elemWidth;
document.getElementById("Cbutton").style.height = elemWidth;
document.getElementById("Dbutton").style.height = elemWidth;
document.getElementById("Ebutton").style.height = elemWidth;
document.getElementById("Fbutton").style.height = elemWidth;
document.getElementById("Gbutton").style.height = elemWidth;
document.getElementById("Hbutton").style.height = elemWidth;
document.getElementById("Ibutton").style.height = elemWidth;
document.getElementById("Jbutton").style.height = elemWidth;
document.getElementById("Kbutton").style.height = elemWidth;
document.getElementById("Lbutton").style.height = elemWidth;
document.getElementById("Mbutton").style.height = elemWidth;
document.getElementById("Nbutton").style.height = elemWidth;
document.getElementById("Obutton").style.height = elemWidth;
document.getElementById("Pbutton").style.height = elemWidth;
document.getElementById("Qbutton").style.height = elemWidth;
document.getElementById("Rbutton").style.height = elemWidth;
document.getElementById("Sbutton").style.height = elemWidth;
document.getElementById("Tbutton").style.height = elemWidth;
document.getElementById("Ubutton").style.height = elemWidth;
document.getElementById("Vbutton").style.height = elemWidth;
document.getElementById("Wbutton").style.height = elemWidth;
document.getElementById("Xbutton").style.height = elemWidth;
document.getElementById("Ybutton").style.height = elemWidth;
document.getElementById("Zbutton").style.height = elemWidth;


function check_letter(character) {
    $.ajax({
        type: "POST",
        url: "/check_letter/",
        dataType: "json",
        data: JSON.stringify({'character': character, 'username' : user_name }),
        contentType: "application/json",
        success: function (data) {
            document.getElementById('current-string').innerHTML = data.current_string
            document.getElementById('hang-man-image').src = "/static/" + data.hang_man_image
            document.getElementById(character + 'button').style.backgroundColor = (data.answer_status == true? '#68ad74' : '#ff6d6d')
            document.getElementById(character + 'button').disabled = true;
            
            show_pop_up(data.win_status, data.answer)
        },
        error: function (data) {
            alert("Failed to connect server!");
        }
    });
}


let intervalId;
function show_pop_up(win_status, answer) {
    if(win_status == "win")
    {
        document.getElementById('popup').style.display = 'block';
        document.getElementById('popup-content').style.backgroundColor = 'green';
        document.getElementById('message-box').innerHTML = "You Won!";
        document.getElementById('timer-result').innerHTML = document.getElementById('timer').innerHTML;

        clearInterval(intervalId);
        $(':button').prop('disabled', true); // Disable all buttons
    }
    else if(win_status == "lose")
    {
        document.getElementById('popup').style.display = 'block';
        document.getElementById('popup-content').style.backgroundColor = 'red';
        document.getElementById('message-box').innerHTML = "You Losed!";
        document.getElementById('timer-result').innerHTML = "correct word: " + answer;

        clearInterval(intervalId);
        $(':button').prop('disabled', true); // Disable all buttons
    }
}

function close_pop_up(win_status) {
    document.getElementById('popup').style.display = 'none';
}

window.onload = function() {
    stopWatch();
}

function stopWatch() {
    let time = 0;
    
    incrementTime();
    intervalId = setInterval(incrementTime, 1000);
    

    function incrementTime() {
        time++;
        document.getElementById("timer").textContent = ("0" + Math.trunc(time / 3600)).slice(-2) + " : " + ("0" + Math.trunc((time % 3600) / 60)).slice(-2) + " : " + ("0" + (time % 60)).slice(-2);
    }
}

// function isMobileDevice() {
//     return (window.innerWidth < 1300) || (navigator.userAgent.indexOf("Mobi") > -1);
// }

// if (navigator.userAgent.indexOf("Mobi") > -1) {
//     document.getElementById('mobile_check').style.display = 'block';
//     document.getElementById('error_text').innerHTML = 'This game is not designed for mobile, please use PC';
// }
// else if (window.innerWidth < 1300) {
//     document.getElementById('mobile_check').style.display = 'block';
//     document.getElementById('error_text').innerHTML = 'Please Full Screen your browser and refresh to open the game!';
// }

// else {
//     document.getElementById('mobile_check').style.display = 'none';
// }