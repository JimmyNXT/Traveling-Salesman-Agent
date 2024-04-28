package loc.mtech.ui.components;

import processing.core.PVector;
import processing.core.PApplet;


public class Button {
    private PVector pos;
    private float width;
    private float height;
    private int colour;
    private String text;
    private Boolean pressed;
    private Boolean clicked;
    private Boolean visible;
    private PApplet applet;

    public Button(PApplet applet, int x, int y, float width, float height, String text, int red, int green, int blue) {
        this.applet = applet;
        this.pos = new PVector();
        this.pos.x = x;
        this.pos.y = y;
        this.width = width;
        this.height = height;
        this.colour = this.applet.color(red, green, blue);
        this.text = text;
        this.pressed = false;
        this.clicked = false;
        this.visible = true;
    }

    public void update() {
        if (this.visible) {
            if ((this.applet.mousePressed) &&
                    (this.applet.mouseButton == this.applet.LEFT) /*&& (!this.pressed)*/) {
                this.pressed = true;
                if (this.applet.mouseX >= this.pos.x && (this.applet.mouseX <= this.pos.x + this.width) && (this.applet.mouseY >= this.pos.y && (this.applet.mouseY <= this.pos.y + this.width))) {
                    this.clicked = true;
                }
            } else {
                this.pressed = false;
                this.clicked = false;
            }
        }
    }

    public void render() {
        this.applet.fill(this.colour);
        this.applet.rect(this.pos.x, this.pos.y, this.width, this.height);
        this.applet.fill(0);
        this.applet.textAlign(this.applet.CENTER, this.applet.CENTER);
        this.applet.text(this.text, this.pos.x + width / 2, this.pos.y + this.height / 2);
    }


    public PVector getPos() {
        return pos;
    }

    public void setPos(PVector pos) {
        this.pos = pos;
    }

    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    public int getColour() {
        return colour;
    }

    public void setColour(int colour) {
        this.colour = colour;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public Boolean getPressed() {
        return pressed;
    }

    public void setPressed(Boolean pressed) {
        this.pressed = pressed;
    }

    public Boolean getClicked() {
        return clicked;
    }

    public void setClicked(Boolean clicked) {
        this.clicked = clicked;
    }

    public Boolean getVisible() {
        return visible;
    }

    public void setVisible(Boolean visible) {
        this.visible = visible;
    }

    public PApplet getApplet() {
        return applet;
    }

    public void setApplet(PApplet applet) {
        this.applet = applet;
    }
}
