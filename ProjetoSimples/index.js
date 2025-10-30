const inputTarefa = document.getElementById("input-tarefa");
const btnAdicionar = document.getElementById("btn-adicionar");
const listaTarefas = document.getElementById("lista-tarefa");



btnAdicionar.addEventListener("click", adicionarTarefa);
inputTarefa.addEventListener("keyup", (event) => {
    if (event.keyCode === 13){
        adicionarTarefa();
    }
})

listaTarefas.addEventListener("click", gerenciarClickLista);

function adicionarTarefa(){
    const textoDaTarefa = inputTarefa.value;
        if (textoDaTarefa == ""){
            alert("Digite um texto válido");
            return;
        }       else{
                    const novoItem = document.createElement("li");
                    const checkList = document.createElement("input");
                    checkList.type = "checkbox";
                    const textoItem = document.createElement("span");
                    textoItem.textContent = textoDaTarefa
                    const btnExcluir = document.createElement("button");
                        btnExcluir.textContent = "X"
                        btnExcluir.classList.add("btn-excluir");
                            novoItem.appendChild(checkList)
                            novoItem.appendChild(textoItem);
                            novoItem.appendChild(btnExcluir);
                    listaTarefas.appendChild(novoItem);
                    inputTarefa.value = "";  
                    inputTarefa.focus();
        }
} 

function gerenciarClickLista(event){
    const alvoClick = event.target;
        if (alvoClick.classList.contains("btn-excluir")){
            alvoClick.parentElement.remove();    
        } else if (alvoClick.type === "checkbox"){
            alvoClick.parentElement.classList.toggle("concluida");
        }
}



