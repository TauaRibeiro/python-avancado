/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package testes;

import pacoteUsuario.Funcionario;
import pacoteUsuario.Cliente;

public class TesteUsuarios {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Funcionario f1 = new Funcionario();
        
        f1.setNome_usuario("Teste");
        f1.setSenha_usuario("123");
        
        try{
            Funcionario.cadastrarFuncionario(f1);
        }catch(InstantiationException e){
            System.out.println("Deu erro");
        }
    }
    
}
