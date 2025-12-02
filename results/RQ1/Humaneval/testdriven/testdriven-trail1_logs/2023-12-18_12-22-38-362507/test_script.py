def sort_third(l: list):
    l_prime = l.copy()
    
    for i in range(0, len(l_prime), 3):
        if i + 3 <= len(l_prime):
            l_prime[i:i+3] = sorted(l_prime[i:i+3])
        else:
            l_prime[i:] = sorted(l_prime[i:])

    return l_prime
import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()