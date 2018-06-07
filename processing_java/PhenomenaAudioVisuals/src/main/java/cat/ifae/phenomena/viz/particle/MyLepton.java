package cat.ifae.phenomena.viz.particle;


import cat.ifae.phenomena.viz.sound.MySynth;
import cat.ifae.phenomena.viz.cicle.CurrentCicle;
import cat.ifae.phenomena.viz.shapes.MyShape;
import cat.ifae.phenomena.viz.shapes.MyWaveRing;
import cat.ifae.phenomena.viz.data.MyParticleData;
import cat.ifae.phenomena.viz.params.MyParams;
import processing.core.PApplet;
import beads.AudioContext;

class MyLepton extends MyParticleFamily{

    public MyLepton(PApplet p, AudioContext ac, float x, float y, MyParticleData particleData){
        super(p, ac, x,y, particleData);
        this.myParams= new MyParams(p, particleData);
        this.currentCicle = new CurrentCicle(p, myParams.lepton.getSpeed());

        addMyShapes();
        addMySounds();
    }

    public MyLepton(PApplet p, float x, float y, MyParticleData particleData){
        super(p, x,y, particleData);
        this.myParams= new MyParams(p, particleData);
        this.currentCicle = new CurrentCicle(p, myParams.lepton.getSpeed());

        addMyShapes();
    }

    @Override
    public void addMyShapes(){
        shapes.add(new MyWaveRing(p,x,y,currentCicle,myParams.lepton));
    }

    @Override
    public void addMySounds(){
        //sounds.add(new MySynth(ac, currentCicle, 440.0f));
    }

    @Override
    public void display(){
        p.text(particleData.getName(), x, y);
        for (MyShape shape: shapes){
            shape.display();
        }
    }

    @Override
    public void sound(){
        for (MySynth sound: sounds){
            sound.ac.start();
        }
    }

    @Override
    public void move(){
        for (MyShape shape: shapes){
            shape.move();
        }
    }
}
