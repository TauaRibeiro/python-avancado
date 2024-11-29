package pacoteLivro;

import java.util.ArrayList;

public class Livro {
    final private static ArrayList<Livro> lista_livro = new ArrayList();
    private String titulo;
    private int quantidade;
    private ArrayList<String> autores = new ArrayList();

    @Override
    public String toString() {
        return "Título: " + titulo + "\nQuantidade: " + quantidade + "\nAutores: " + autores + '\n';
    }
    
    
    public Livro(){
        this.titulo = null;
        this.quantidade = 0;
        this.autores = null;
           
    }

    public static ArrayList<Livro> getLista_livro() {
        return lista_livro;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) throws IllegalArgumentException{
        if(titulo.length() < 3){
            throw new IllegalArgumentException("O título deve ter no mínimo 3 carcteres");
        }else{
            this.titulo = titulo;
        }
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) throws IllegalArgumentException{
        if(quantidade <= 0){
            throw new IllegalArgumentException("A quantidade deve ser maior que 0");
        }else{
            this.quantidade = quantidade;
        }
    }

    public ArrayList<String> getAutores() {
        return autores;
    }

    public void setAutor(String autor) throws IllegalArgumentException{
        if(autor.length() < 3){
            throw new IllegalArgumentException("O nome do autor deve ter no mínimo 3 caracteres");
        }else{
            this.autores.add(autor);
        }
    }
    
    public static void cadastrarLivro(Livro l) throws InstantiationException{
        if(l.autores.isEmpty() || l.quantidade < 0 || l.titulo == null){
            throw new InstantiationException("Livro inválido!");
        }else{
            lista_livro.add(l);
        }
    }
    
    public static String exibirLivros (String titulo){
        if(lista_livro.isEmpty()){
            return "Não há livros cadastrados...";
        }
        
        StringBuilder resultado = new StringBuilder();
        
        for(Livro l:lista_livro){
            if(titulo.equalsIgnoreCase(l.titulo)){
                resultado.append(l.toString());
            }
        }
        
        return (resultado.isEmpty())? "Livro não encontrado":resultado.toString();
    }
    
    public static String exibirLivros (){
        if(lista_livro.isEmpty()){
            return "Não há livros cadastrados...";
        }

        StringBuilder resultado = new StringBuilder();

        for(Livro l:lista_livro){
            resultado.append(l.toString());
        }

        return (resultado.isEmpty())? "Livro não encontrado":resultado.toString();
    }
}
