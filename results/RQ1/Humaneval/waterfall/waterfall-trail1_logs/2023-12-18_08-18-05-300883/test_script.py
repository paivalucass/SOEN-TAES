def will_it_fly(q, w):
    if not isinstance(q, list) or not isinstance(w, int) or w <= 0:
        raise ValueError("Invalid input. Please provide a list as the first argument and a positive integer as the second argument.")

    if not q:
        return True

    if q != q[::-1]:
        return False

    if sum(q) <= w:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()