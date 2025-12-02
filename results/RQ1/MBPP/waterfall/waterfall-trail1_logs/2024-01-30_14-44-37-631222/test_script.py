def big_diff(nums):
    try:
        if len(nums) == 0:
            raise ValueError("Error: Input list is empty")
        elif len(nums) == 1:
            return 0
        elif any(not isinstance(num, (int, float)) for num in nums):
            raise ValueError("Error: Input list contains non-numeric values")
        else:
            max_num = max(nums)
            min_num = min(nums)
            return max_num - min_num
    except ValueError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()