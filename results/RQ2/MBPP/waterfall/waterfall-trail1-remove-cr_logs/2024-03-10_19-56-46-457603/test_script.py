def volume_cube(side_length):
    if side_length <= 0:
        raise ValueError("Side length should be a positive number")
    volume = side_length ** 3
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()