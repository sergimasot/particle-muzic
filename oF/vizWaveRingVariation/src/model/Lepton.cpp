#include "Lepton.h"

Lepton::Lepton(shared_ptr<ParticleData>& _particleData):Model(_particleData){
};

void Lepton::buildParameters(){
  string name = data -> getName();
  shapes_num = 1;
  after_img = 8;
  segments = 100;
  radius = 200;
  pos_amp.set(radius/4,radius/4,radius);
  rot_amp.set(0,0,0);
  if (name == "e-"){
      speed_amp = 0.05;
      noiseStep = 0;
      noiseAmount = 0;
      width = 0;
      framesPerCycle = 80;
  }
  else if (name== "mu-"){
      speed_amp = 0.02;
      noiseStep = 0.04;
      noiseAmount = 17;
      width = 14;
      framesPerCycle = 128;
  }
  else if (name == "tau-"){
      speed_amp = 0.01;
      noiseStep = 0.3;
      noiseAmount = 74;
      width = 14;
      framesPerCycle = 200;
  }
  getColorMode();
}


bool Lepton::getColorMode(){
  col_mode = 0;

}
