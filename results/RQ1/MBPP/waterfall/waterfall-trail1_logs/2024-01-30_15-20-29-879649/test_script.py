def find_Element(arr, ranges, rotations, index):
    if not arr:
        return "Error: Empty array"
    n = len(arr)
    for r in ranges:
        start = r[0]
        end = r[1]
        if start < 0 or end >= n:
            return "Error: Invalid rotation ranges"
        arr[start:end+1] = arr[start:end+1][::-1]

    rotations = rotations % n
    arr = arr[-rotations:] + arr[:-rotations]

    if index < 0 or index >= n:
        return "Error: Index out of bounds"
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()