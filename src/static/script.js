const msgerForm = document.getElementById("form");
const msgerInput = document.getElementById("form-input");
const msgerChat = document.getElementById("msgerChat");

const BOT_NAME = "Minerva";
const PERSON_NAME = "User";

msgerForm.addEventListener("submit", event => {
    event.preventDefault();

    const msgText = msgerInput.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, "right", msgText);
    msgerInput.value = "";

    botResponse(msgText);
});

var suggestion_buttons = document.querySelectorAll('.autosubmit');
var inputField = document.getElementById('form-input');

suggestion_buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        var buttonText = this.textContent;
        inputField.value = buttonText;
        document.getElementById('send-msg').click();
    });
});

document.getElementById("QuerySub").addEventListener('click', function() {
    var buttonText = this.textContent;
    inputField.value = buttonText;
});

function appendMessage(name, side, text) {
    const msgHTML = `
    <div class="msg ${side}-msg">
        <div class="msg-bubble">
        <div class="msg-info">
            <div class="msg-info-name">${name}</div>
        </div>

        <div class="msg-text">${text}</div>
        </div>
    </div>
    `;

    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
}

function botResponse(input) {
    // get response from Minerva
    fetch("/get", {method: "POST", body: JSON.stringify({"msg":input})})
	.then(response => response.json())
	.then(data => {
        appendMessage(BOT_NAME, "left", data.msg);
    });
}

function loadDatabase(){
    var dropdown_selection = document.getElementById("dropdown").value;
    DB_change(dropdown_selection);

    if(dropdown_selection == "medical.sql"){
        document.getElementById("medical.sql").style.display = "none";
        document.getElementById("financial.sql").style.display = "inline";
        document.getElementById("loadedDB").innerHTML = "Metabolic Syndrome";
    }
    else{
        document.getElementById("medical.sql").style.display = "inline";
        document.getElementById("financial.sql").style.display = "none";
        document.getElementById("loadedDB").innerHTML = "Stock Market Data";
    }


    close_DBSelect()
    switch_Colour()
}

function DB_change(file){
    fetch("/database", {method: "POST", body: JSON.stringify({"db_name":file})})
}

function get(selector, root = document) {
    return root.querySelector(selector);
}

document.getElementById("closeButton").addEventListener("click", function(){
    close_DBSelect();
});

document.getElementById("floater").addEventListener("click", function() {
    var floatingElement = document.getElementById("floatingElement");
    var overlay = document.getElementById("overlay");

    floatingElement.style.opacity = 100;
    overlay.style.opacity = 100;

    floatingElement.classList.remove("hidden");
    overlay.classList.remove("hidden");
});

function close_DBSelect(){
    var floatingElement = document.getElementById("floatingElement");
    var overlay = document.getElementById("overlay");

    floatingElement.style.opacity = 0;
    overlay.style.opacity = 0;

    setTimeout(() => {  
        floatingElement.classList.add("hidden")
        overlay.classList.add("hidden");
    }, 800)
}

function switch_Colour(){
    const root = document.documentElement;
    var style = getComputedStyle(document.body);

    if (style.getPropertyValue('--dark') == '#00334E') {
        root.style.setProperty('--dark', '#801010'); // Red Dark
        root.style.setProperty('--med', '#AA1414'); // Red Med
        root.style.setProperty('--light', '#C33939'); // Red Light
        root.style.setProperty('--body-bg', 'url("media/background_red.png")')
    } else {
        root.style.setProperty('--dark', '#00334E'); // Blue Dark
        root.style.setProperty('--med', '#145374'); // Blue Med
        root.style.setProperty('--light', '#5588A3'); // Blue Light
        root.style.setProperty('--body-bg', 'url("media/background_blue.png")')
    }
}

window.onload = function(){ 
    DB_change("");
    div = document.getElementById("hideAll");

    div.ontransitionend = () => {
        div.style.display = "none";
    };

    setTimeout(() => {  
        div.style.opacity = 0;
    }, 1500)
}