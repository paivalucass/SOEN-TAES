def min_Jumps(steps, d):
    x, y = steps
    distance = ((x - d)**2 + y**2)**0.5
    jumps = distance / d
    return round(jumps, 1)
import unittest

class Test(unittest.TestCase):
    def test_min_Jumps(self):
        self.assertEqual(min_Jumps((3,4), 11), 3.5)

if __name__ == '__main__':
    unittest.main()