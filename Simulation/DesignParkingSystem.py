# In this problem, we're asked to design a simple parking system for a parking lot with three different types of parking spaces: big, medium, and small.
# Each type of parking space has a fixed number of slots that can be occupied by cars of that specific size. The parking system needs to be able to handle two operations:
# Initializing the parking system with the number of slots for each type of parking space.
#   Adding a car to the parking lot, which is subject to there being an available slot for the car's type.
#   When a car tries to park, the parking system checks if there is an available slot for that particular size of the car. If an appropriate slot is available, the car parks (i.e., the count of available slots of that type reduces by one), and the system returns true. If no slot is available for that car's type, the system returns false.
# Simulating Coding Problem
# Time Complexity: O(1) Space Complexity: O(1)
from typing import List


class ParkingSystem:
  def __init__(self, big: int, medium: int, small: int):
    self.parking_lot: List[int] = [0, big, medium, small]

  def add_car(car_type: int) -> bool:
    if self.parking_lot[car_type]:
      self.parking_lot[car_type] -= 1
      return True
    return False
