def find_First_Missing(array, start=0, end=None):
    for i in range(len(array)):
        if array[i] != i:
            return i
    return len(array)
import unittest

class Test(unittest.TestCase):
    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()