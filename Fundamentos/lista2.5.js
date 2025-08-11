let nomes = ['Gustavo', 'Millena', 'Guilherme', 'Gisele', 'Silvana', 'Vilson'];

function TemNome(array, nome){
    for (let i = 0; i < array.length; i++){
        if (array[i] === nome){
            console.log(`${nome} está no array`);
            return true
        }
    }

    console.log(`${nome} não esta no array`);
    return false;
}    
    
   

TemNome(nomes, 'Millena');
TemNome(nomes, 'Gabriel');
TemNome(nomes, 'Silvana');
TemNome(nomes, 'Gustavo');


