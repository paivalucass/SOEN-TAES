def big_sum(nums):
    try:
        if len(nums) == 0:
            raise ValueError("Error: Empty array")
        for num in nums:
            if not isinstance(num, (int, float)):
                raise TypeError("Error: Non-numeric inputs")
        
        min_val = min(nums)
        max_val = max(nums)
        return min_val + max_val
    
    except ValueError as ve:
        return str(ve)
    
    except TypeError as te:
        return str(te)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()