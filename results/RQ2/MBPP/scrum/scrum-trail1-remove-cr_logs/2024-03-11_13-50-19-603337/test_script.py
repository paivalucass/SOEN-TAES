def find_First_Missing(array,start=0,end=None):
    if not array or array[0] != 0:
        return 0

    for i in range(len(array) - 1):
        if array[i+1] - array[i] > 1:
            return array[i] + 1

    return array[-1] + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()