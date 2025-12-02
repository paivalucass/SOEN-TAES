import math
from typing import Union

def volume_cone(r: float, h: float) -> Union[float, str]:
    '''
    Calculate the volume of a cone.

    Parameters:
    r (float): radius of the cone
    h (float): height of the cone

    Returns:
    Union[float, str]: volume of the cone or error message

    Raises:
    ValueError: if r or h is not a positive number
    '''

    if r <= 0 or h <= 0:
        return "Invalid input for radius or height"

    volume = (1/3) * math.pi * (r ** 2) * h
    return round(volume, 15)  # rounding to 15 decimal places for comparison

# Test cases
assert math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=0.001)
assert volume_cone(0, 12) == "Invalid input for radius or height"
assert volume_cone(5, 0) == "Invalid input for radius or height"
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()