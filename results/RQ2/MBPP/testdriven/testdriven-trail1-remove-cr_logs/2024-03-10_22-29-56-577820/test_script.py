def Find_Min_Length(lst):
    if not isinstance(lst, list) or not all(isinstance(x, list) for x in lst):
        raise ValueError("Input should be a list of lists")
        
    if not lst:
        return 0
    
    min_length = float('inf')
    for l in lst:
        if len(l) < min_length:
            min_length = len(l)
    
    return min_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()