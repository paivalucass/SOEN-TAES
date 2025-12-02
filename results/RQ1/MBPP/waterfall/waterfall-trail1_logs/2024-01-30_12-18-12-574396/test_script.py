def find_volume(length, breadth, height):
    if length <= 0 or breadth <= 0 or height <= 0:
        return "Length, breadth, and height must be positive numbers."

    if not all(isinstance(i, (int, float)) for i in [length, breadth, height]):
        return "Length, breadth, and height must be numeric."

    volume = length * breadth * height / 2
    return volume
import unittest

class Test(unittest.TestCase):
    def test_find_volume(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()