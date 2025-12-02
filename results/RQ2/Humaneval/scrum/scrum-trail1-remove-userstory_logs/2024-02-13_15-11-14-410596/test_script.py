def will_it_fly(q, w):
    if not isinstance(q, list):
        return "Error: Input q should be a list"
    if q != q[::-1]:
        return False
    if sum(q) > w:
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_will_it_fly(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()