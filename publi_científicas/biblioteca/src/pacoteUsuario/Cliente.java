/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pacoteUsuario;

import java.util.ArrayList;

public class Cliente extends Usuario{
    final private static ArrayList<Cliente> lista_Clientes = new ArrayList();
    
    public Cliente(){
        super();
    }

    public static ArrayList<Cliente> getLista_Clientes() {
        return lista_Clientes;
    }
    
    public static void cadastrarCliente(Cliente c) throws InstantiationException{
        if(c.nome_usuario == null || c.senha_usuario == null){
            throw new InstantiationException("Cliente inválido");
        }else{
            lista_Clientes.add(c);
            lista_usuarios.add(c);
        }
    }
}
