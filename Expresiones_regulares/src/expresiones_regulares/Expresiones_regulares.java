
package expresiones_regulares;


import java.awt.Dimension;
import java.awt.Toolkit;
import javax.swing.JFrame;


public class Expresiones_regulares {

    public static void main(String[] args){
        
        Ventana p = new Ventana();
		p.setVisible(true);
        p.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        p.setResizable(false);       
                       
        Toolkit vent= Toolkit.getDefaultToolkit();
        Dimension tam= vent.getScreenSize();
        int alto= tam.height;
        int ancho= tam.width;
        System.out.println(alto);
        System.out.println(ancho);
        
        p.setSize(683, 500);
        p.setLocation(384, 130);
    }
    
}
