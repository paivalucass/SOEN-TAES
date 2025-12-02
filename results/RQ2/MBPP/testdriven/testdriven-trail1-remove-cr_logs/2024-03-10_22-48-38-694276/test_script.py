def find_First_Missing(array, start=0, end=None):
    sorted_array = sorted(array)
    if end is None:
        end = len(array)
    for i in range(start, end):
        if sorted_array[i] != i:
            return i
    return end
import unittest

class Test(unittest.TestCase):
    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()