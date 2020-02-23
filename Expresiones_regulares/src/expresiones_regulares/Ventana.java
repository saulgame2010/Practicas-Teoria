
package expresiones_regulares;

import java.awt.BorderLayout;
import java.awt.Color;
import javax.swing.*;
import java.awt.event.*;
import java.sql.*;
import java.util.regex.*;

public class Ventana extends JFrame implements ActionListener {

    Icon insertar, error,at,contraseña,id;
    JLabel jUsuario, jPass, jCorreo, jCurp, fondo;
    JTextField tUsuario, tPass, tCorreo, tCurp;
    JButton registrar;
    ConexionBD conexion;
    Connection con;
    Pattern pCorreo, pCurp, pPass;
    Matcher mCorreo, mCurp, mPass;
    String usuario, pass, correo, curp;
    //JPanel fondoo, componentes;

    public Ventana() {
        
        PanelImagen fondo = new PanelImagen();
        this.add(fondo, BorderLayout.CENTER); 
        fondo.setLayout(null);
        setSize(683, 500);
        setVisible(true);
        conexion = new ConexionBD();
        con = conexion.Conectate();
        pCorreo = Pattern.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`"
                + "{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*"
                + "[a-z0-9])?");
        pCurp = Pattern.compile("[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}"
                + "(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])" + "[HM]{1}"
                + "(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)"
                + "[B-DF-HJ-NP-TV-Z]{3}" + "[0-9A-Z]{1}[0-9]{1}$");
        pPass = Pattern.compile("(?=\\w*\\d)(?=\\w*[A-Z])(?=\\w*[a-z])\\S{8,16}$");       

        jUsuario = new JLabel("Usuario: ");
        jUsuario.setBounds(150, 50, 70, 30);
        jUsuario.setForeground(Color.WHITE);
        fondo.add(jUsuario);

        /*debe tener al entre 8 y 16 caracteres, al menos un dígito, 
                al menos una minúscula y al menos una mayúscula, puede tener otros simbolos.*/
        jPass = new JLabel("Contraseña: ");
        jPass.setBounds(150, 100, 100, 30);
        jPass.setForeground(Color.WHITE);
        fondo.add(jPass);

        jCorreo = new JLabel("Correo: ");
        jCorreo.setBounds(150, 150, 50, 30);
        jCorreo.setForeground(Color.WHITE);
        fondo.add(jCorreo);

        jCurp = new JLabel("CURP: ");
        jCurp.setBounds(150, 200, 50, 30);
        jCurp.setForeground(Color.WHITE);
        fondo.add(jCurp);

        tUsuario = new JTextField();
        tUsuario.setBounds(240, 50, 135, 30);
        fondo.add(tUsuario);

        tPass = new JTextField();
        tPass.setBounds(240, 100, 135, 30);
        fondo.add(tPass);

        tCorreo = new JTextField();
        tCorreo.setBounds(240, 150, 135, 30);
        fondo.add(tCorreo);

        tCurp = new JTextField();
        tCurp.setBounds(240, 200, 135, 30);
        fondo.add(tCurp);

        registrar = new JButton("Registrar");
        registrar.setBounds(150, 300, 100, 20);
        registrar.setBackground(Color.BLACK);
        registrar.setBorderPainted(false);
        registrar.setForeground(Color.WHITE);
        registrar.addActionListener(this);
        fondo.add(registrar);

        this.setTitle("Registro de usuarios");

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        insertar = new ImageIcon("src/img/add.png");
        error = new ImageIcon("src/img/error.png");
        at=new ImageIcon("src/img/at.png");
        contraseña=new ImageIcon("src/img/pass.png");
        id=new ImageIcon("src/img/id.png");
        
        usuario = tUsuario.getText();
        pass = tPass.getText();
        correo = tCorreo.getText();
        curp = tCurp.getText();
        mCorreo = pCorreo.matcher(correo);
        mCurp = pCurp.matcher(curp);
        mPass = pPass.matcher(pass);
        
        if(mPass.find()==false){
            JOptionPane.showMessageDialog(null,"Formato de contraseña incorrecto","Atención",
                    JOptionPane.WARNING_MESSAGE,contraseña);
            tPass.setText("");   
        }
        if(mCorreo.find()==false){
            JOptionPane.showMessageDialog(null,"Formato de correo incorrecto","Atención",
                    JOptionPane.WARNING_MESSAGE,at);
            tCorreo.setText("");
        }
        if(mCurp.find()==false){
            JOptionPane.showMessageDialog(null,"Formato de curp incorrecto","Atención",
                    JOptionPane.WARNING_MESSAGE,id);
            tCurp.setText("");
        }
        usuario = tUsuario.getText();
        pass = tPass.getText();
        correo = tCorreo.getText();
        curp = tCurp.getText();
        mCorreo = pCorreo.matcher(correo);
        mCurp = pCurp.matcher(curp);
        mPass = pPass.matcher(pass);
        

        String query = "INSERT INTO Usu"
                + "(usuario, pass, correo, curp) VALUES"
                + "(?, ?, ?, ?)";
        if (mCorreo.find() && mCurp.find() && mPass.find()) {
            try {
                PreparedStatement ps = con.prepareStatement(query);
                ps.setString(1, usuario);
                ps.setString(2, pass);
                ps.setString(3, correo);
                ps.setString(4, curp);

                ps.executeUpdate();
                JOptionPane.showMessageDialog(null, "Se insertaron los datos", "Verificacion",
                        JOptionPane.WARNING_MESSAGE, insertar);
                Registros vista=new Registros();
                vista.setLocationRelativeTo(null);
                vista.setResizable(false); 
                vista.setVisible(true);
                dispose();
            } catch (SQLException s) {
                JOptionPane.showMessageDialog(null, "Hubo un error " + s, "",
                        JOptionPane.WARNING_MESSAGE, error);
            }
        } 
        
    }
}
