def largest_neg(input_list):
    if not input_list:
        return None
    max_neg = None
    for num in input_list:
        if num < 0:
            if max_neg is None or num < max_neg:
                max_neg = num
    return max_neg
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()