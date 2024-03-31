package loc.mtech;

import loc.mtech.domain.components.Button;
import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import processing.core.PApplet;

public class Main extends PApplet {
    private static final Logger logger = LogManager.getLogger(Main.class.getName());
    private Button bnt1;

    public static void main(String[] args) {
        PApplet.main(java.lang.invoke.MethodHandles.lookup().lookupClass());

    }

    @Override
    public void settings() {
        size(800, 800);
        this.bnt1 = new Button(this, 10, 10 ,100, 50, "Test", 0, 255, 0);
    }

    @Override
    public void setup() {
//        colorMode(HSB, 1, 1, 1, 1);
//        frameRate(144);
    }

    @Override
    public void draw() {
        this.bnt1.render();
        this.bnt1.update();
        if(this.bnt1.getClicked()){
            this.bnt1.setColour(this.color(255, 0, 0));
            logger.log(Level.DEBUG, "Clicked");
        }else{
            this.bnt1.setColour(this.color(0, 255, 0));
        }

    }
}