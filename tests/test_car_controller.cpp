#include <gtest/gtest.h>
#include "car_controller.h"

TEST(CarControllerTest, InitTest) {
  CarController carController;
  carController.init();
  // Assertions to verify initialization
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
// This test suite initializes the CarController and checks if it can be initialized correctly.
// You can add more tests to check the functionality of the CarController methods.