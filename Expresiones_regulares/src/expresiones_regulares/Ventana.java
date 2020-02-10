
package expresiones_regulares;

import javax.swing.*;
import java.awt.event.*;
import java.sql.*;
import java.util.regex.*;

public class Ventana extends JFrame implements ActionListener{

	JLabel jUsuario, jPass, jCorreo, jCurp;
	JTextField tUsuario, tPass, tCorreo, tCurp;
	JButton registrar;
	ConexionBD conexion;
	Connection con;
	Pattern pCorreo;
	Matcher mCorreo;
	String usuario, pass, correo, curp;

	public Ventana() {
		conexion = new ConexionBD();
		con = conexion.Conectate();
		pCorreo = Pattern.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`"
                        + "{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*"
                        + "[a-z0-9])?");


		this.getContentPane().setLayout(null);		

		jUsuario = new JLabel("Usuario");
		jUsuario.setBounds(150, 50, 50, 30);
		this.add(jUsuario);

		jPass = new JLabel("Contraseña, con al menos una "
			+"letra mayuscula y al menos un numero");
		jPass.setBounds(150, 100, 50, 30);
		this.add(jPass);

		jCorreo = new JLabel("Correo");
		jCorreo.setBounds(150, 150, 50, 30);
		this.add(jCorreo);

		jCurp = new JLabel("CURP");
		jCurp.setBounds(150, 200, 50, 30);
		this.add(jCurp);

		tUsuario = new JTextField();
		tUsuario.setBounds(300, 50, 80, 20);
		this.add(tUsuario);

		tPass = new JTextField();
		tPass.setBounds(300, 100, 80, 20);
		this.add(tPass);

		tCorreo = new JTextField();
		tCorreo.setBounds(300, 150, 80, 20);
		this.add(tCorreo);

		tCurp = new JTextField();
		tCurp.setBounds(300, 200, 80, 20);
		this.add(tCurp);

		registrar = new JButton("Registrar");
		registrar.setBounds(150, 300, 100, 20);
        registrar.addActionListener(this);
		this.add(registrar);

		this.setTitle("Registro de usuarios");
	}

    @Override
    public void actionPerformed(ActionEvent e) {        

        usuario = tUsuario.getText();
        pass = tPass.getText();
        correo = tCorreo.getText();
        curp = tCurp.getText();
        mCorreo = pCorreo.matcher(correo);

        String query = "INSERT INTO Usu"
        + "(usuario, pass, correo, curp) VALUES"
        + "(?, ?, ?, ?)";
        if(mCorreo.find()) {
        	try {
        		PreparedStatement ps = con.prepareStatement(query);
        		ps.setString(1, usuario);
        		ps.setString(2, pass);
        		ps.setString(3, correo);
        		ps.setString(4, curp);

        		ps.executeUpdate();
        		JOptionPane.showMessageDialog(null, "Se insertaron los datos");
        	} catch(SQLException s) {
        		JOptionPane.showMessageDialog(null, "Hubo un error " + s);
        	}
        } else {
        	JOptionPane.showMessageDialog(null, "Formato invalido");
        }
    }
}