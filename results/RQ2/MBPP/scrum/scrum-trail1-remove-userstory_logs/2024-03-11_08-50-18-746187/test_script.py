def find_Volume(length, base, height):
    if type(length) not in [int, float] or type(base) not in [int, float] or type(height) not in [int, float]:
        raise TypeError("Invalid input types")
    if length <= 0 or base <= 0 or height <= 0:
        raise ValueError("All input parameters must be positive numbers")
    
    volume = (1.0/2.0) * length * base * height
    return round(volume, 2) if volume != 0 else 0.5

'''Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240'''
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()