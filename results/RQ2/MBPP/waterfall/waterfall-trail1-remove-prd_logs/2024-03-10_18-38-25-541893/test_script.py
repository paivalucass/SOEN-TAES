def neg_nos(list1):
    if not list1:
        return "Error: Empty input list"

    if not all(isinstance(num, (int, float)) for num in list1):
        return "Error: Non-numeric values found in input list"

    neg_numbers = [num for num in list1 if num < 0]

    if not neg_numbers:
        return "No negative numbers found"

    return neg_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(neg_nos([-1, 4, 5, -6]), [-1, -6])

if __name__ == '__main__':
    unittest.main()