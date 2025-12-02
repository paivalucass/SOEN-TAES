def sort_numeric_strings(nums_str):
    if not isinstance(nums_str, list) or not all(isinstance(x, str) and x.lstrip('-').isdigit() for x in nums_str):
        raise ValueError("Input must be a list of strings containing only numeric characters")

    sorted_nums = sorted(nums_str, key=lambda x: int(x))
    sorted_integers = [int(x) for x in sorted_nums]
    return sorted_integers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']), [-500, -12, 0, 4, 7, 12, 45, 100, 200])

if __name__ == '__main__':
    unittest.main()