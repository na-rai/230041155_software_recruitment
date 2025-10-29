
#ifndef MOTOR_H 
#define MOTOR_H

#include <Arduino.h>

class Motor {
  private:
    int pin1, pin2; 
    
  public:
    Motor(int p1, int p2);
    void forward(int speed);
    void backward(int speed);
    void stop();
};

#endif 