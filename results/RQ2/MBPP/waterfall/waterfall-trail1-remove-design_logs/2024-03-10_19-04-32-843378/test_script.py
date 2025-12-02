def pos_count(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    count = sum(1 for num in lst if num > 0)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pos_count([1,-2,3,-4]), 2)

if __name__ == '__main__':
    unittest.main()