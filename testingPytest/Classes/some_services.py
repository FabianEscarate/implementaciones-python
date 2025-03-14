import time
from .calculator import Calculator
from .data_service import DataService

class SomeServices:
  def __init__(self, calculator_service: Calculator = None):
    if calculator_service is None:
      calculator_service = Calculator()
    self.calculator_service = calculator_service
    self.data_service = DataService()

  def perform_action(self):
    print("Performing action")

  async def async_add(self, a: int, b: int) -> int:
    time.sleep(5)
    return self.calculator_service.add(a, b)

  async def async_subtract(self, a: int, b: int) -> int:
    time.sleep(5)
    return self.calculator_service.subtract(a, b)

  async def async_multiply(self, a: int, b: int) -> int:
    time.sleep(5)
    return self.calculator_service.multiply(a, b)

  async def async_divide(self, a: int, b: int) -> float:
    time.sleep(5)
    return self.calculator_service.divide(a, b)
  
  async def async_get_data(self):
    time.sleep(5)
    return self.data_service.get_data()