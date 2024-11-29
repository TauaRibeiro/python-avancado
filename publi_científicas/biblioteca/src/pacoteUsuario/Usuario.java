package pacoteUsuario;

import java.util.ArrayList;

public class Usuario {
    final static protected ArrayList<Usuario> lista_usuarios = new ArrayList();
    static protected int GERADOR_ID = 1;
    protected int id_usuario;
    protected String nome_usuario;
    protected String senha_usuario;
    
    public Usuario(){
        this.nome_usuario = null;
        this.senha_usuario = null;
        
        this.id_usuario = GERADOR_ID++;
    }

    public int getId_usuario() {
        return id_usuario;
    }

    public String getNome_usuario() {
        return nome_usuario;
    }

    public void setNome_usuario(String nome_usuario) throws IllegalArgumentException{
        if(nome_usuario.length() < 3){
            throw new IllegalArgumentException("O nome deve ter no mínimo 3 caracteres");
        }else{
            this.nome_usuario = nome_usuario;
        }
    }

    public String getSenha_usuario() {
        return senha_usuario;
    }

    public void setSenha_usuario(String senha_usuario) throws IllegalArgumentException{
        if(senha_usuario.length() < 4){
            throw new IllegalArgumentException("A senha deve ter no mínimo 4 caracteres.");
        }else{
            this.senha_usuario = senha_usuario;
        }
    }
}
