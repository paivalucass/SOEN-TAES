def find_Element(arr, ranges, rotations, index):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return "Invalid input for arr"
    if not isinstance(ranges, list) or not all(isinstance(x, list) and len(x) == 2 for x in ranges):
        return "Invalid input for ranges"
    if not isinstance(rotations, int) or rotations < 0:
        return "Invalid input for rotations"
    if not isinstance(index, int) or index < 0:
        return "Invalid input for index"

    n = len(arr)
    arr = arr[index % n:] + arr[:index % n]

    for r in ranges:
        start = r[0] % n
        end = r[1] % n
        arr = arr[start:end] + arr[:start] + arr[end:]

    return arr[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()