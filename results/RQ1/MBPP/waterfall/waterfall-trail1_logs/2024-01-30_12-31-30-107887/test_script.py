def merge_sorted_list(num1, num2, num3):
    if not num1 or not num2 or not num3:
        raise ValueError("Input lists cannot be empty")
    
    merged_list = num1 + num2 + num3
    sorted_list = sorted(merged_list)
    
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]), [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233])

if __name__ == '__main__':
    unittest.main()