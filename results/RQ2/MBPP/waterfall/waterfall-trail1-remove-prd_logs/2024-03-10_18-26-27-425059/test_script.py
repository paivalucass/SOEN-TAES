def pos_count(lst):
    if not lst or not all(isinstance(x, int) for x in lst):
        return "Error: Input list is either empty or does not contain only integers"
    
    count = sum(1 for num in lst if num > 0)
    
    return count
import unittest

class Test(unittest.TestCase):
    def test_pos_count(self):
        self.assertEqual(pos_count([1, -2, 3, -4]), 2)

if __name__ == '__main__':
    unittest.main()