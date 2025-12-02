def min_Jumps(steps, d):
    total_steps = abs(steps[0]) + abs(steps[1])
    if total_steps == 0:
        if d == 0:
            return 0
        else:
            return "Invalid Input"
    else:
        return float(abs(d) / total_steps)
import unittest

class Test(unittest.TestCase):
    def test_min_Jumps(self):
        self.assertEqual(min_Jumps((3, 4), 11), 3.5)

if __name__ == '__main__':
    unittest.main()