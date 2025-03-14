import pytest
from Classes.calculator import Calculator

def test_sum():
  assert Calculator.add(1, 2) == 3
  assert Calculator.add(-1, 1) == 0
  assert Calculator.add(-1, -1) == -2

def test_sustract():
  assert Calculator.subtract(10, 5) == 5
  assert Calculator.subtract(-1, 1) == -2
  assert Calculator.subtract(-1, -1) == 0

def test_multiply():
  assert Calculator.multiply(3, 7) == 21
  assert Calculator.multiply(-1, 1) == -1
  assert Calculator.multiply(-1, -1) == 1

def test_division():
  assert Calculator.divide(10, 2) == 5
  assert Calculator.divide(-1, 1) == -1
  assert Calculator.divide(-1, -1) == 1
  with pytest.raises(ZeroDivisionError):
    Calculator.divide(1, 0)