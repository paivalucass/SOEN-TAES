def larg_nnum(input_list, n):
    if not isinstance(input_list, list) or not all(isinstance(x, (int, float)) for x in input_list) or not isinstance(n, int) or n < 0:
        return "Invalid input: input_list must be a list of numbers and n must be a non-negative integer"
    
    if n >= len(input_list):
        return sorted(input_list, reverse=True)
    else:
        return sorted(input_list, reverse=True)[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2), [100, 90])

if __name__ == '__main__':
    unittest.main()