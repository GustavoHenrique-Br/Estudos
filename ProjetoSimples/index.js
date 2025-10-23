const inputTarefa = document.getElementById("input-tarefa");
const btnAdicionar = document.getElementById("btn-adicionar");
const listaTarefas = document.getElementById("lista-tarefa");

btnAdicionar.addEventListener("click", adicionarTarefa);
inputTarefa.addEventListener("keyup", (event) => {
    if (event.keyCode === 13){
        adicionarTarefa();
    }
})

function adicionarTarefa(){
    const textoDaTarefa = inputTarefa.value;
        if (textoDaTarefa == ""){
            alert("Digite um texto válido");
            return;
        }       else{
                    const novoItem = document.createElement("li");
                    novoItem.textContent = textoDaTarefa;
                    listaTarefas.appendChild(novoItem);
                    inputTarefa.value = "";
                    inputTarefa.focus();

            
        }

} 
