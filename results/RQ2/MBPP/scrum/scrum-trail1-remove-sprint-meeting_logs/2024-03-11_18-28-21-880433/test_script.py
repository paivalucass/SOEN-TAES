def volume_cube(l):
    if not isinstance(l, (int, float)):
        raise ValueError("Side length must be a number")
    if l <= 0:
        raise ValueError("Side length should be a positive number")

    volume = l ** 3
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()