def largest_neg(list1):
    if not list1:
        return "Input list is empty"

    max_neg = None
    for num in list1:
        if num < 0:
            if max_neg is None or num < max_neg:
                max_neg = num

    if max_neg is None:
        return "No negative numbers found in the input list"

    return max_neg
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_neg([1,2,3,-4,-6]), -6)

if __name__ == '__main__':
    unittest.main()