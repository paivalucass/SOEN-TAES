def find_Element(arr, ranges, rotations, index):
    for _ in range(rotations):
        element = arr.pop(0)
        arr.append(element)
    for r in ranges:
        start, end = r
        arr = arr[start:end+1]
    if index < 0 or index >= len(arr):
        return -1
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5], [[0,2],[0,3]], 2, 1), 3)

if __name__ == '__main__':
    unittest.main()