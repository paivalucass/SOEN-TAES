def find_First_Missing(array, start=0, end=None):
    if not array:
        return start
    seen = set(array)
    for i in range(start, end or max(array) + 1):
        if i not in seen:
            return i
    return end or max(array) + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()