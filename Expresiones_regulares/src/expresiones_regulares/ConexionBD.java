
package expresiones_regulares;

import java.sql.*;
import javax.swing.*;

public class ConexionBD {
    public String bd = "Expresiones";
	public String url = "jdbc:mysql://localhost:3307/" + bd;
	public String usuario = "root";
	public String pass = "";

	public Connection Conectate() {

       Connection link = null;

       try{

           Class.forName("org.gjt.mm.mysql.Driver");

           link = DriverManager.getConnection(this.url, this.usuario, this.pass);

       }catch(Exception ex){

           JOptionPane.showMessageDialog(null, ex);

       }

       return link;
   
	}
}
