def neg_nos(list1):
    if not isinstance(list1, list):
        return "Error: Input must be a list"

    negative_numbers = [num for num in list1 if isinstance(num, int) and num < 0]

    return negative_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(neg_nos([-1,4,5,-6]), [-1,-6])

if __name__ == '__main__':
    unittest.main()