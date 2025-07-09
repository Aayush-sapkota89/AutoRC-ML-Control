import unittest
from unittest.mock import patch, MagicMock
from car_interface import CarInterface

class TestCarInterface(unittest.TestCase):
  @patch('serial.Serial')
  def test_move_forward(self, mock_serial):
    car = CarInterface()
    car.move_forward()
    mock_serial.return_value.write.assert_called_once_with(b'F')

if __name__ == '__main__':
  unittest.main()
# This test suite uses unittest and unittest.mock to test the CarInterface class.
# It mocks the serial.Serial class to avoid actual hardware interaction.