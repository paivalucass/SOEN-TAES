def median_numbers(a, b, c):
    if not all(isinstance(num, (int, float)) for num in [a, b, c]):
        raise ValueError("Input should be three numbers")
    
    if len(set([a, b, c])) != 3:
        raise ValueError("Input values should be distinct")
    
    nums = [a, b, c]
    nums.sort()
    return nums[1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25,55,65), 55.0)

if __name__ == '__main__':
    unittest.main()