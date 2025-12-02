def Extract(lst):
    result = []
    if not lst:
        return "Input list is empty"
    for sublist in lst:
        if isinstance(sublist, list) and len(sublist) > 0:
            result.append(sublist[0])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()