#include <Arduino.h>
#include "car_controller.h"

CarController carController;

void setup() {
  carController.init();
}

void loop() {
  carController.update();
  delay(100);
}
// This is the main entry point for the firmware. It initializes the car controller
// and enters a loop where it continuously updates the car's state.