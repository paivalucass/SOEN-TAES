def find_Element(arr, ranges, rotations, index):
    n = len(arr)
    for i in range(rotations):
        x = arr.pop(-1)
        arr.insert(0, x)
    result = []
    for r in ranges:
        start, end = r
        result.extend(arr[start:end + 1])
    if index < len(result):
        return result[index]
    else:
        return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()