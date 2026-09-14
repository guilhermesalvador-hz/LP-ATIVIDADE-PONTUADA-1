/*const form = document.getElementById('imcForm');
const resultado = document.getElementById('resultado');

form.addEventListener('input', () => {
    resultado.textContent = '';
    resultado.style.display = 'none';
});

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const pesoValor = Number(document.getElementById('peso').value);
    const alturaValor = Number(document.getElementById('altura').value);

    if (pesoValor <= 0 || alturaValor <= 0) {
        resultado.textContent = 'O peso e a altura devem ser maiores que zero.';
        resultado.style.display = 'block'; // mostra a mensagem de erro também
        return;
    }

    const imc = pesoValor / (alturaValor * alturaValor);

    resultado.textContent = `Seu IMC é: ${imc.toFixed(2)}`;
    resultado.style.display = 'block'; // mostra o resultado
}); */

// ===== DOM =====
// ===== DOM =====
const form = document.getElementById('imcForm');
const pesoInput = document.getElementById('peso');
const alturaInput = document.getElementById('altura');
const resultado = document.getElementById('resultado');

// ===== AÇÃO =====
function classificarIMC(imc) {
    if (imc < 18.5) return 'Abaixo do peso';
    if (imc < 25) return 'Peso ideal';
    if (imc < 30) return 'Sobrepeso';
    if (imc < 35) return 'Obesidade grau I';
    if (imc < 40) return 'Obesidade grau II';
    return 'Obesidade grau III';
}

function calcularIMC() {
    const peso = Number(pesoInput.value);
    const altura = Number(alturaInput.value);

    if (peso <= 0 || altura <= 0) {
        resultado.textContent = 'O peso e a altura devem ser maiores que zero.';
        resultado.style.display = 'block';
        return;
    }

    const imc = peso / (altura * altura);
    const classificacao = classificarIMC(imc);

    resultado.textContent = `Seu IMC é: ${imc.toFixed(2)} — ${classificacao}`;
    resultado.style.display = 'block';
}

function limparResultado() {
    resultado.textContent = '';
    resultado.style.display = 'none';
}

// ===== EVENTO =====
form.addEventListener('submit', (event) => {
    event.preventDefault();
    calcularIMC();
});

form.addEventListener('input', limparResultado);