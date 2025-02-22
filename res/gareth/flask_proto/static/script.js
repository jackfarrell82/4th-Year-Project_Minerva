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

function get(selector, root = document) {
    return root.querySelector(selector);
}

window.onload = function(){ 
    div = document.getElementById("hideAll")

    div.ontransitionend = () => {
        div.style.display = "none";
    };

    setTimeout(() => {  
        div.style.opacity = 0;
    }, 2000)
}