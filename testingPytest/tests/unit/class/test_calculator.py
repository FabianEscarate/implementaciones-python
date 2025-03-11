import pytest
from Classes.calculator import Calculator

def test_sum():
  assert Calculator.sum(1, 2) == 3
  assert Calculator.sum(-1, 1) == 0
  assert Calculator.sum(-1, -1) == -2

def test_sustract():
  assert Calculator.sustract(10, 5) == 5
  assert Calculator.sustract(-1, 1) == -2
  assert Calculator.sustract(-1, -1) == 0

def test_multiply():
  assert Calculator.multiply(3, 7) == 21
  assert Calculator.multiply(-1, 1) == -1
  assert Calculator.multiply(-1, -1) == 1

def test_division():
  assert Calculator.division(10, 2) == 5
  assert Calculator.division(-1, 1) == -1
  assert Calculator.division(-1, -1) == 1
  with pytest.raises(ZeroDivisionError):
    Calculator.division(1, 0)