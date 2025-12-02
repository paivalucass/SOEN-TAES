def find_volume(l, b, h):
    if l <= 0 or b <= 0 or h <= 0:
        return "Invalid input"
    else:
        volume = l * b * h
        return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()