def Find_Min_Length(lst):
    if not all(isinstance(x, list) for x in lst):
        raise ValueError("Input is not a list of lists")

    if len(lst) == 0:
        return 0
    
    min_length = len(lst[0])
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