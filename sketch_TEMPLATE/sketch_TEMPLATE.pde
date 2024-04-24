public class Entity2D{
    public Vector2 position = new Vector2();
    public Entity2D(){};
    public Entity2D(Vector2 position){
        this.position = position;
    }
    public Entity2D(float x, float y){
        this.position = new Vector2(x,y);
    }
    public void Draw(){
        
    }
}


void draw(){
    background(0, 0, 0);
}

void setup(){
    size(1920,1080);
    
}