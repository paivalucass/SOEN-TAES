def pos_count(lst):
    count = 0
    if not isinstance(lst, list) or len(lst) == 0:
        return 0
    
    for num in lst:
        if num > 0:
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pos_count([1,-2,3,-4]), 2)

if __name__ == '__main__':
    unittest.main()