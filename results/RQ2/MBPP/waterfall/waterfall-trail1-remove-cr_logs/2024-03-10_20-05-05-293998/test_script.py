def neg_nos(list1):
    if not list1 or all(num >= 0 for num in list1):
        return []
    return [num for num in list1 if num < 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(neg_nos([-1, 4, 5, -6]), [-1, -6])

if __name__ == '__main__':
    unittest.main()