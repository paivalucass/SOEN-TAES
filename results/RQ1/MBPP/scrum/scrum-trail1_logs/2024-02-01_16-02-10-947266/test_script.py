def digit_distance_nums(n1, n2):
    n1_str = str(n1)
    n2_str = str(n2)
    
    max_len = max(len(n1_str), len(n2_str))
    n1_str = n1_str.zfill(max_len)
    n2_str = n2_str.zfill(max_len)
    
    total_diff = 0
    for digit1, digit2 in zip(n1_str, n2_str):
        total_diff += abs(int(digit1) - int(digit2))
    
    return total_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()