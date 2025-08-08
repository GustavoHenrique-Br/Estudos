let numeros = ['3', '12', '39', '57', '25', '98'];



function TemPar(array){
    let contadorPar = 0;

    for (let i = 0; i < array.length; i++){
        let numero = Number(array[i]);
        
        if (numero % 2 === 0){
            contadorPar++;
        }
    }
        if (contadorPar >= 1){
            console.log(`Há pelo menos um numero par`);  
            return true;         
        } else {
            console.log(`Não possui um numero par`);
            return false
        }

}

TemPar(numeros);