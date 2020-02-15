package expresiones_regulares;

import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.ImageIcon;
import javax.swing.JPanel;

public class PanelImagen extends JPanel{
 
    @Override
    public void paintComponent(Graphics g){
        Dimension tam=getSize();
        ImageIcon imagen= new ImageIcon(new ImageIcon(getClass().getResource("/img/fondo.png")).getImage());
        g.drawImage(imagen.getImage(),0,0,tam.width,tam.height,null);
        setOpaque(false);
        super.paintComponent(g);
    }
}
