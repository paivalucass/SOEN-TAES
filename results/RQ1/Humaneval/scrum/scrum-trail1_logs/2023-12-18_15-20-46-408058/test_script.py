def is_palindromic_list(q):
    mid = len(q) // 2
    if len(q) % 2 == 0:
        return q[:mid] == q[mid:][::-1]
    else:
        return q[:mid] == q[mid+1:][::-1]

def will_it_fly(q, w):
    if not isinstance(q, list) or not isinstance(w, int) or w < 0:
        return False  # Input validation for q and w

    if not is_palindromic_list(q) or sum(q) > w:
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()