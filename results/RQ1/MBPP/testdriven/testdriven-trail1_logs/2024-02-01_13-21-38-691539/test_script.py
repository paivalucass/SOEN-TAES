def sort_numeric_strings(nums_str):
    try:
        nums_int = [int(x) for x in nums_str]
        nums_int.sort()
        return nums_int
    except ValueError:
        raise ValueError("Input list contains non-numeric strings")

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']), [-500, -12, 0, 4, 7, 12, 45, 100, 200])

if __name__ == '__main__':
    unittest.main()