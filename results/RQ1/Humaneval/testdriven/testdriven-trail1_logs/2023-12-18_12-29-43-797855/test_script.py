def will_it_fly(q, w):
    if not isinstance(q, list) or not all(isinstance(x, (int, float)) for x in q):
        return False
    
    if len(q) == 0:
        return False
    
    is_palindromic = q == q[::-1]
    sum_of_elements = sum(q)
    
    if is_palindromic and sum_of_elements <= w:
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