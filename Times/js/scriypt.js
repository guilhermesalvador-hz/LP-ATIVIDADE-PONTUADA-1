const home = document.querySelector('.home');
const botoes = document.querySelectorAll('.buttons button');

botoes.forEach(function(botao) {
    botao.addEventListener('click', function() {
        home.src = botao.dataset.img;
    });
});