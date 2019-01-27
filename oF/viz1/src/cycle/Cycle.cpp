#include "Cycle.h"

Cycle::Cycle(int _framesPerCycle):framesPerCycle(_framesPerCycle){
  frameRate = ofGetTargetFrameRate(); // or ofGetFrameRate()
  hz = frameRate/framesPerCycle;
  progressRatioMax = (float) (framesPerCycle-1)/framesPerCycle;
}

void Cycle::update(){
  int frameNum = ofGetFrameNum();
  currentCycle = (float) frameNum/(float) framesPerCycle;
  currentFrame = frameNum%framesPerCycle;
  progressRatio = (float) currentFrame/(float) framesPerCycle;
  QuadEaseInRatio = pow(progressRatio,2);
  QuadEaseOutRatio = 1-pow(progressRatio-1,2)+1;
  QuartEaseInRatio = pow(progressRatio,4);
  QuartEaseOutRatio = 1-pow(progressRatio-1,4)+1;
  SextEaseInRatio = pow(progressRatio,6);
  SextEaseOutRatio = 1-pow(progressRatio-1,6)+1;
}

float Cycle::getEase(){
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = 1-QuadEaseInRatio;}
  else {ease = 1-QuadEaseOutRatio;}
  return ease;
}

float Cycle::getEase2(){
  update();
  float ease = 0;
  if (progressRatio <= 0.5){ease = QuadEaseOutRatio;}
  else {ease = 1-QuartEaseInRatio;}
  return ease;
}

void Cycle::newNoiseSeed(){
  if (progressRatio == progressRatioMax){
    return ofSeedRandom();
  }
}

bool Cycle::newLoop(){
  update();
  bool newcycle = false;
  if (progressRatio == progressRatioMax){
      newcycle = true;
  }
  return newcycle;
}

int Cycle::getCurrentFrame(){
  return currentFrame;
}


float Cycle::getQuadIn(){
  return QuadEaseInRatio;
}

float Cycle::getQuadOut(){
  return QuadEaseOutRatio;
}

float Cycle::getQuartIn(){
  return QuartEaseInRatio;
}

float Cycle::getQuartOut(){
  return QuartEaseOutRatio;
}

float Cycle::getSextIn(){
  return SextEaseInRatio;
}

float Cycle::getSextOut(){
  return SextEaseOutRatio;
}

void Cycle::setFramesPerCycle(int _framesPerCycle){
  framesPerCycle = _framesPerCycle;
}