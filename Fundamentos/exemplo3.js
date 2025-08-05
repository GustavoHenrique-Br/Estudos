function ehMaior(idade) {
    if (idade >= 18)
        return true;
    return false;
}

const teste1EhMaior = ehMaior(15);
console.log("Testando se teste1 é de maior: ");
if (teste1EhMaior == true) {
    console.log("teste1 é maior de idade");
} else {
    console.log("teste1 é menor de idade");
}

const teste2EhMaior = ehMaior(19);
console.log("Testando se teste2 é de maior: ");
if (teste2EhMaior == true) {
    console.log("teste2 é maior de idade");
} else {
    console.log("teste2 é menor de idade");
}
