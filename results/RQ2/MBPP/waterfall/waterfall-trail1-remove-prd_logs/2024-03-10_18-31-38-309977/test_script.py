def volume_cube(l):
    if not isinstance(l, (int, float)) or l <= 0:
        return "Error: Invalid input"
    return round(l ** 3, 9) if l > 0 else 0

assert volume_cube(3)==27
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()