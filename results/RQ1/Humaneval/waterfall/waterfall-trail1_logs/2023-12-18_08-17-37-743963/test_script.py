def search(lst):
    if any(num <= 0 for num in lst):
        return -1
    
    max_freq = -1
    result = -1
    
    for num in lst:
        freq = lst.count(num)
        if freq >= num and num > result:
            result = num
    
    return result

import unittest

class Test(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()