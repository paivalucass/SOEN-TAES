def is_palindromic_list(q):
    return q == q[::-1]

def will_it_fly(q, w):
    if not isinstance(q, list):
        raise ValueError("Input q must be a list of integers")
    if not isinstance(w, int):
        raise ValueError("Input w must be an integer")

    if not q:
        return False
    
    if not is_palindromic_list(q):
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