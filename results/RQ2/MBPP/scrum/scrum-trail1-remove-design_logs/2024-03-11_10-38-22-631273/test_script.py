def neg_nos(list1):
    if not isinstance(list1, list):
        raise TypeError("Input must be a list")

    result = [num for num in list1 if num < 0]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(neg_nos([-1,4,5,-6]), [-1,-6])

if __name__ == '__main__':
    unittest.main()