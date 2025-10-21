const carro = {
    marca: "Chevrolet", 
    modelo: "Agile",
    ano: 2011,
    placa: "ENY-9026",
    buzina: function(){console.log(`biiiiiiii`);},
    completo: function(){
        return "A marca do carro é "+this.marca+ " e o modelo é "+this.modelo;
    }
};

console.log(carro.completo());