def Extract(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of sublists")
    result = [sublist[0] if sublist else "Error: Empty sublist" for sublist in lst]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()