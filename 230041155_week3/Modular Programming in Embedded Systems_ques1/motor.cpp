
#include "motor.h" 
#include <Arduino.h> 
Motor::Motor(int p1, int p2) {
  pin1 = p1; 
  pin2 = p2;  
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
}


void Motor::forward(int speed) {
  analogWrite(pin1, speed); 
  analogWrite(pin2, 0);      
}

void Motor::backward(int speed) {
  analogWrite(pin1, 0);     
  analogWrite(pin2, speed);  
}
void Motor::stop() {
  analogWrite(pin1, 0);  
  analogWrite(pin2, 0);  

}
