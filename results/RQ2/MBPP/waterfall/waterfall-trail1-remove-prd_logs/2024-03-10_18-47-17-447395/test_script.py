def sort_numeric_strings(nums_str):
    if not nums_str:
        raise ValueError("Input cannot be empty")
    
    nums = [int(num) for num in nums_str if num.lstrip('-').isdigit()]
    if not nums:
        raise ValueError("No valid numeric strings found in input")
    
    sorted_nums = sorted(nums)
    return sorted_nums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']), [-500, -12, 0, 4, 7, 12, 45, 100, 200])

if __name__ == '__main__':
    unittest.main()