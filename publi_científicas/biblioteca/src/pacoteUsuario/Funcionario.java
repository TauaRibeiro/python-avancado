package pacoteUsuario;

import java.util.ArrayList;

public class Funcionario extends Usuario{
    final private static ArrayList<Funcionario> lista_funcionarios = new ArrayList();
    
    public Funcionario(){
        super();
    }

    public static ArrayList<Funcionario> getLista_funcionarios() {
        return lista_funcionarios;
    }
    
    public static void cadastrarFuncionario(Funcionario f) throws InstantiationException{
        if(f.nome_usuario == null || f.senha_usuario == null){
            throw new InstantiationException("Funcionario inválido");
        }else{
            lista_funcionarios.add(f);
            lista_usuarios.add(f);
        }
    }
}
