def zero_count(input_list):
    zero_count = 0
    non_zero_count = 0
    
    if len(input_list) == 0:
        return None
    elif not all(isinstance(x, int) for x in input_list):
        return "Error"
    
    for num in input_list:
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
            
    if non_zero_count == 0:
        return 1.0
    else:
        try:
            return round(zero_count / non_zero_count, 6)
        except ZeroDivisionError:
            return "Error"
import unittest
import math

class Test(unittest.TestCase):
    def test_zero_count(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, places=6)

if __name__ == '__main__':
    unittest.main()