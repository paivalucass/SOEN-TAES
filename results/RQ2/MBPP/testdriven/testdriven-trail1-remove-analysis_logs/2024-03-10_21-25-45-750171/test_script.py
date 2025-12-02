def find_First_Missing(array, start=0, end=None):
    if not array:
        return 0
    if end is None:
        end = len(array)
    while start < end:
        mid = start + (end - start) // 2
        if array[mid] == mid:
            start = mid + 1
        else:
            end = mid
    return start

import unittest

class Test(unittest.TestCase):
    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()