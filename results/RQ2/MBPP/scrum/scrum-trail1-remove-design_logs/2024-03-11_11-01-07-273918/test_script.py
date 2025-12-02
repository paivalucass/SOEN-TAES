def find_First_Missing(array, start=0, end=None):
    if end is None:
        end = len(array)
    if not array or (start > end) or (start < 0) or (end < 0) or (start > len(array)) or (end > len(array)):
        return None
    for i in range(start, end):
        if array[i] != i:
            return i
    return end
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()