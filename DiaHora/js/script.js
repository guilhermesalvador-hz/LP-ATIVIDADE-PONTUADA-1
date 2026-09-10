const horas = document.getElementById('horas');
const minutos = document.getElementById('minutos');
const segundos = document.getElementById('segundos');
const elementoDia = document.getElementById('dia');
const elementoMes = document.getElementById('mes');
const elementoAno = document.getElementById('ano');

function atualizarPainel() {
    const agora = new Date();

    
    const h = String(agora.getHours()).padStart(2, '0');
    const m = String(agora.getMinutes()).padStart(2, '0');
    const s = String(agora.getSeconds()).padStart(2, '0');

    horas.textContent = h;
    minutos.textContent = m;
    segundos.textContent = s;

    
    const dia = String(agora.getDate()).padStart(2, '0');
    const mes = String(agora.getMonth() + 1).padStart(2, '0');
    const ano = agora.getFullYear();

    elementoDia.textContent = dia;
    elementoMes.textContent = mes;
    elementoAno.textContent = ano;
}


atualizarPainel();
setInterval(atualizarPainel, 1000);
