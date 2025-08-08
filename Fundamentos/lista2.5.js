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

TemNome(nomes, 'Millena');
TemNome(nomes, 'Gabriel');
TemNome(nomes, 'Silvana');
TemNome(nomes, 'Gustavo');


