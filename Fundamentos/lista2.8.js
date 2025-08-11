let alunos = ['Gustavo', 'Millena', 'Gabriel', 'Guilherme', 'Gisele', 'Heitor', 'Silvana', 'Vilson', 'Lucas'];
const prompt = require("prompt-sync")();

function Chamada(lista){
    let AlunosPresentes = [];
    let AlunosAusentes = []
    
    for (let i = 0; i < lista.length; i++){
        let ChamadaAlunos = prompt(`O aluno ${lista[i]} está presente? S/N `);
            if (ChamadaAlunos === `S`){
                AlunosPresentes.push(lista[i]);
            }   else if (ChamadaAlunos === `N`){
                AlunosAusentes.push(lista[i]);
            }   else {
                console.log(`Digito inválido, pressione S ou N`);
                i--
            }
    }
    console.log(`Alunos presentes: `, AlunosPresentes);
    console.log(`Alunos ausentes`, AlunosAusentes);

    return AlunosPresentes
}

Chamada(alunos);


