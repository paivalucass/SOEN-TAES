def min_Jumps(steps, d):
    '''Write a function to check for the number of jumps required of given length to reach a point of form (d, 0) from origin in a 2d plane.'''
    x = d / steps[0]
    y = steps[1] / steps[0]
    return x + (y * (d - (x * steps[0])) / steps[1])
import unittest

class Test(unittest.TestCase):
    def test_min_jumps(self):
        self.assertEqual(min_Jumps((3,4), 11), 3.5)

if __name__ == '__main__':
    unittest.main()