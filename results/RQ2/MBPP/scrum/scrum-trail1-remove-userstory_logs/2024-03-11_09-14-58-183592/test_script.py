def digit_distance_nums(n1, n2):
    n1_str = str(n1)
    n2_str = str(n2)
    
    if len(n1_str) != len(n2_str):
        raise ValueError("Input integers must have the same number of digits")
    
    sum_diff = 0
    for digit1, digit2 in zip(n1_str, n2_str):
        diff = abs(int(digit1) - int(digit2))
        sum_diff += diff
    
    return sum_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()