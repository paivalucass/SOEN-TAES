def Extract(lst):
    result = []
    for sublist in lst:
        if isinstance(sublist, list) and sublist:
            result.append(sublist[0])
        else:
            raise ValueError('Error: Input does not meet design specifications')
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]), [1, 3, 6])

if __name__ == '__main__':
    unittest.main()