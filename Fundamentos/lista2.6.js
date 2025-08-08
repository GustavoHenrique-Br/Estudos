let nomes = ['Gustavo', 'Millena', 'Guilherme', 'Gisele', 'Silvana', 'Vilson'];

function TemNome(array, nome){
    if (array.includes(nome)){
        console.log(`${nome} está no array`);
        return true;
    } else {
        console.log(`${nome} não está no array`);
        return false;
    }
}

const prompt = require('prompt-sync')();
const nome = prompt("Qual o seu nome?");
TemNome(nomes, nome);


