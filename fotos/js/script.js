//DOM object model

const alvo = document.querySelector("#alvo");
const btyabem = document.querySelector("#bt1");
const btcr7 = document.querySelector("#bt2");
const btpessi = document.querySelector("#bt3");

//Event listeners
btyabem.addEventListener('click',yabem)
btcr7.addEventListener('click',the cr7)
btpessi.addEventListener('click',pessi)




// açao

function yabem() {
    alvo.src = "img/yabem.jpg";
}

function the cr7() {
    alvo.src = "img/cr7.jpg";
}

function pessi() {
    alvo.src = "img/pessi.jpg";
}
