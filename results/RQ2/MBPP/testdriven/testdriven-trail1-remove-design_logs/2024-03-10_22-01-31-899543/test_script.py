def volume_cube(side_length):
    if not isinstance(side_length, (int, float)):
        return "Error: Non-numeric value"
    if side_length < 0:
        return "Error: Negative side length"
    return side_length ** 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()