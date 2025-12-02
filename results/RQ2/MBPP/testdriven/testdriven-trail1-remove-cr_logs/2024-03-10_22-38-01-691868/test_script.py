def find_Element(arr, ranges, rotations, index):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("Input array must be a list of integers")
    if not isinstance(ranges, list) or not all(isinstance(x, list) and len(x) == 2 for x in ranges):
        raise ValueError("Ranges must be a list of lists with 2 elements")
    if not isinstance(rotations, int) or rotations < 0:
        raise ValueError("Number of rotations must be a non-negative integer")
    if not isinstance(index, int) or index < 0 or index >= len(arr):
        raise ValueError("Index must be a non-negative integer within the range of the input array")

    for r in range(rotations):
        temp = arr.pop()
        arr.insert(0, temp)

    result_index = (index - rotations) % len(arr)
    result = arr[result_index]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()