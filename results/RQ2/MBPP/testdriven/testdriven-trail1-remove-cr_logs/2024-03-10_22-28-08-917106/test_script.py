def smallest_num(xs):
    if not xs:
        raise ValueError("Input list is empty")
    
    unique_list = list(set(xs))
    smallest = min(unique_list)
    
    return smallest

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()