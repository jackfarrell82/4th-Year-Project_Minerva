const BOT_NAME = "Minerva";
const PERSON_NAME = "User";
SQL_FLAG = "off"; // flag to control is SQL is shown to user

// MESSAGE SUBMISSION

const msgerForm = document.getElementById("form");
const msgerInput = document.getElementById("form-input");
const msgerChat = document.getElementById("msgerChat");

msgerForm.addEventListener("submit", event => {
    event.preventDefault();

    const msgText = msgerInput.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, "right", msgText); // add the message they typed to screen
    msgerInput.value = "";

    botResponse(msgText); // get a bot response from Minerva
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
    // get response from Minerva, send user msg back to python code
    fetch("/get", {method: "POST", body: JSON.stringify({"msg":input, "sql":SQL_FLAG})})
	.then(response => response.json())
	.then(data => {
        appendMessage(BOT_NAME, "left", data.msg); // append Minerva's response
    });
}

// SUGGESTION BUTTONS

var suggestion_buttons = document.querySelectorAll('.autosubmit');
var inputField = document.getElementById('form-input');

// each button adds their text to the typing box if clicked and sends it
suggestion_buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        var buttonText = this.textContent;
        inputField.value = buttonText;
        document.getElementById('send-msg').click();
    });
});

// Query adds the "Query:" text but doesn't send the message
document.getElementById("QuerySub").addEventListener('click', function() {
    var buttonText = this.textContent;
    inputField.value = buttonText;
});


// DATABASE INFORMATION POPUPS

function showMetaInfo() {
    var otherpopup = document.getElementById("StockPopup");
    otherpopup.classList.remove("show");
    var popup = document.getElementById("MetaPopup");
    popup.classList.toggle("show");

    setTimeout(() => {  
        popup.classList.remove("show")
    }, 7000)
}

function showStockInfo() {
    var otherpopup = document.getElementById("MetaPopup");
    otherpopup.classList.remove("show");
    var popup = document.getElementById("StockPopup");
    popup.classList.toggle("show");

    setTimeout(() => {  
        popup.classList.remove("show")
    }, 7000)
}

// CHANGING DATABASE

// called when a new option is selected
function loadDatabase(){
    var dropdown_selection = document.getElementById("dropdown").value;
    DB_change(dropdown_selection); // change DB in backend

    if(dropdown_selection == "medical.sql"){
        document.getElementById("medical.sql").style.display = "none";
        document.getElementById("financial.sql").style.display = "inline";
        document.getElementById("loadedDB").innerHTML = "Metabolic Syndrome";
    }
    else{
        document.getElementById("medical.sql").style.display = "inline";
        document.getElementById("financial.sql").style.display = "none";
        document.getElementById("loadedDB").innerHTML = "Stock Market Index";
    }


    close_DBSelect() // close menu
    switch_Colour() // switch website colours
}

function DB_change(file){ // sends msg to python to change database
    fetch("/database", {method: "POST", body: JSON.stringify({"db_name":file})})
}

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

// BUTTONS AND ICONS

document.getElementById("info-icon").addEventListener("click", function(){
    var overlay = document.getElementById("overlay");
    var element = document.getElementById("helpFloater")
    
    overlay.style.opacity = 100;
    overlay.classList.remove("hidden");

    element.style.opacity = 100;
    element.classList.remove("hidden");
});

document.getElementById("closeButtonH").addEventListener("click", function(){
    var element = document.getElementById("helpFloater");
    var overlay = document.getElementById("overlay");

    element.style.opacity = 0;
    overlay.style.opacity = 0;

    setTimeout(() => {  
        element.classList.add("hidden")
        overlay.classList.add("hidden");
    }, 800)
});

document.getElementById("floater").addEventListener("click", function() {
    var floatingElement = document.getElementById("floatingElement");
    var overlay = document.getElementById("overlay");

    floatingElement.style.opacity = 100;
    overlay.style.opacity = 100;

    floatingElement.classList.remove("hidden");
    overlay.classList.remove("hidden");
});

document.getElementById("closeButton").addEventListener("click", function(){
    close_DBSelect();
});

function clearChat(){
    document.getElementById("msgerChat").innerHTML = '<div class="msg left-msg">                <div class="msg-bubble"> <div class="msg-info"><div class="msg-info-name">Minerva  </div> </div><div class="msg-text">    Hello, welcome, my name is Minerva 👋</div></div></div>'
}

document.getElementById("SQLButton").addEventListener("click", function(){
    stat = document.getElementById("SQLStatus")
    
    if(stat.innerHTML == "check"){
        stat.innerHTML = "close"
        stat.style.color = "red"
        SQL_FLAG = "off"
    }
    else{
        stat.innerHTML = "check"
        stat.style.color = "green"
        SQL_FLAG = "on"
    }
    console.log(SQL_FLAG);

});


// when the page loads do this, show the loading screen then fade it out
window.onload = function(){ 
    div = document.getElementById("hideAll");

    div.ontransitionend = () => {
        div.style.display = "none";
    };

    setTimeout(() => {  
        div.style.opacity = 0;
    }, 1500)
}