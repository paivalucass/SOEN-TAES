def Extract(lst):
    if not isinstance(lst, list) or not all(isinstance(sublist, list) for sublist in lst):
        return "Error: Input must be a list of sublists"
    
    try:
        return [sublist[0] for sublist in lst]
    except IndexError:
        return "Error: Sublists must contain at least one element"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()