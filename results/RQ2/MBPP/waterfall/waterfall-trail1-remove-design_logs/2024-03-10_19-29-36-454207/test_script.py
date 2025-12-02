def Find_Min_Length(lst):
    if not lst or not all(isinstance(sublist, list) for sublist in lst):
        raise ValueError("Input list should not be empty and should only contain list elements")

    return min(len(sublist) for sublist in lst)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min_Length([[1],[1,2]]), 1)

if __name__ == '__main__':
    unittest.main()