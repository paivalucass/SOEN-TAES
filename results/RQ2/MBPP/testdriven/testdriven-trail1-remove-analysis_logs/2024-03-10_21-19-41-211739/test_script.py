def neg_nos(list1, return_negative=True):
    if not isinstance(list1, list) or not list1:
        return "Input is not a list or the list is empty"

    result = [num for num in list1 if return_negative and num < 0 or not return_negative and num > 0]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(neg_nos([-1, 4, 5, -6]), [-1, -6])

if __name__ == '__main__':
    unittest.main()