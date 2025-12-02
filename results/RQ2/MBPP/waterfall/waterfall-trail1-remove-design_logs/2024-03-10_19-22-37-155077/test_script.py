def find_First_Missing(array, start=0, end=None):
    if end is None:
        end = len(array)

    if not array or not all(isinstance(i, int) and i > 0 for i in array):
        return 1

    for i in range(start, end):
        if array[i] != i+1:
            return i+1

    return end + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()