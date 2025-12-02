def is_palindromic(lst):
    return lst == lst[::-1]

def is_sum_less_than_w(lst, w):
    return sum(lst) <= w

def will_it_fly(q, w):
    if is_palindromic(q) and is_sum_less_than_w(q, w):
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