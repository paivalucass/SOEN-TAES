def Extract(lst):
    if not lst:
        return []
    if any(len(sublist) != len(lst[0]) for sublist in lst):
        raise ValueError("Sublists are not of equal length")
    return [sublist[0] for sublist in lst]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()