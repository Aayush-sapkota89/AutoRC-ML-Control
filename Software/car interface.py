import serial

class CarInterface:
  def __init__(self):
    self.serial = serial.Serial('COM3', 9600)  # Adjust COM port as necessary

  def connect(self):
    # Establish connection (if needed)
    pass

  def move_forward(self):
    self.serial.write(b'F')

  def move_backward(self):
    self.serial.write(b'B')

  def turn_left(self):
    self.serial.write(b'L')

  def turn_right(self):
    self.serial.write(b'R')

  def stop(self):
    self.serial.write(b'S')

  def disconnect(self):
    self.serial.close()