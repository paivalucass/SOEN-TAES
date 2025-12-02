def volume_cube(l):
    if l <= 0:
        raise ValueError("Input parameter l must be a positive number")
    volume = l**3
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()