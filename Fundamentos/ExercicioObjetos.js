const livro = {
    titulo: "O pequeno Principe",
    Autor: "Antoine de Saint-Exupéry",
    ano: 1943,
    escrito: function(){
        return "O livro " +this.titulo+ " foi escrito por "+this.Autor+" em "+this.ano;
    }
}

console.log(livro.escrito());