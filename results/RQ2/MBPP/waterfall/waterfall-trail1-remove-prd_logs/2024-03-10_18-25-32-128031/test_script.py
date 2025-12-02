def find_volume(length, base, height):
    if length <= 0 or base <= 0 or height <= 0:
        raise ValueError("Length, base, and height must be positive numbers")
    volume = length * base * height
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()