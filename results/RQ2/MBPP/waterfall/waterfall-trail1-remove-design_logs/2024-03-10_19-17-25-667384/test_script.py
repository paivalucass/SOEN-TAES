def find_min(lst):
    if not lst:
        return "Error: Empty list input"
    return min(lst, key=len)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()