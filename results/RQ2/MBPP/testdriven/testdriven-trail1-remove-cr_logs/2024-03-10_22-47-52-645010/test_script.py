def min_Jumps(steps, d):
    '''Write a function to calculate the number of jumps required to reach a point of given length (d, 0) from the origin in a 2D plane.'''
    if not all(isinstance(i, (int, float)) for i in steps) or not isinstance(d, (int, float)):
        raise ValueError("Invalid input. Please provide valid input for steps and d.")

    if any(i <= 0 for i in steps) or d <= 0:
        raise ValueError("Number of steps and distance should be greater than 0.")

    if not all(isinstance(i, int) for i in steps) or not isinstance(d, int):
        raise ValueError("Steps and distance should be integers.")

    jumps = d / sum(steps)
    return round(jumps, 2)
import unittest

class Test(unittest.TestCase):
    def test_min_Jumps(self):
        self.assertEqual(min_Jumps((3,4), 11), 3.5)

if __name__ == '__main__':
    unittest.main()