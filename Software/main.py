import car_interface

def main():
  car = car_interface.CarInterface()
  car.connect()
  while True:
    command = input("Enter command (F/B/L/R/S): ")
    if command.upper() == 'F':
      car.move_forward()
    elif command.upper() == 'B':
      car.move_backward()
    elif command.upper() == 'L':
      car.turn_left()
    elif command.upper() == 'R':
      car.turn_right()
    elif command.upper() == 'S':
      car.stop()
    else:
      print("Invalid command")

if __name__ == "__main__":
  main()
# End of file
# --- END OF FILE ---