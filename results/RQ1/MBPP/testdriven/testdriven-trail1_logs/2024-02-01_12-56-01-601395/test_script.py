def Find_Max_Length(lst):
    if not isinstance(lst, list) or not all(isinstance(sublist, list) for sublist in lst):
        raise ValueError("Input must be a list of lists")
    
    max_length = 0
    for sublist in lst:
        length = len(sublist)
        if length > max_length:
            max_length = length
    return max_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()