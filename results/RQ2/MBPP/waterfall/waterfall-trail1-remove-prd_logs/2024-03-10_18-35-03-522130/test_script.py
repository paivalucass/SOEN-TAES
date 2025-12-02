def find_Element(arr, ranges, rotations, index):
    n = len(arr)
    rotations = rotations % n
    arr = arr[n - rotations:] + arr[:n - rotations]
    result = []
    for r in ranges:
        start = r[0]
        end = r[1] + 1
        result += arr[start:end]
    return result[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()