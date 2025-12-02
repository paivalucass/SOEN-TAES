def count_Occurrence(tup, lst):
    if not isinstance(tup, tuple) or not isinstance(lst, list):
        raise TypeError("Input parameters must be a tuple and a list")
    
    if not tup or not lst:
        raise ValueError("Input parameters cannot be empty")
    
    total_count = 0
    for element in lst:
        count = tup.count(element)
        total_count += count
    
    return total_count
import unittest

class Test(unittest.TestCase):
    def test_count_Occurrence(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()