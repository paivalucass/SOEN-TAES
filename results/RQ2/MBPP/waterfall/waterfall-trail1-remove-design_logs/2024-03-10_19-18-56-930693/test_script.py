def digit_distance_nums(n1, n2):
    if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
        raise ValueError("Both n1 and n2 must be numbers")
    return abs(n1 - n2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()