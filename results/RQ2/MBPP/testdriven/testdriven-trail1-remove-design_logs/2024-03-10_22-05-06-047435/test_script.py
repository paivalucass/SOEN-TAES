def find_element(arr, ranges, rotations, index):
    try:
        if not arr:
            raise ValueError("Array is empty")
        if arr is None:
            raise ValueError("Invalid input array")
        if not all(isinstance(x, int) for x in arr):
            raise ValueError("Invalid input array")
        if rotations < 0:
            raise ValueError("Invalid number of rotations")
        if index < 0 or index >= len(arr):
            raise ValueError("Index out of range")
        for r in ranges:
            if r[0] < 0 or r[1] >= len(arr):
                raise ValueError("Invalid range values")

        # Perform rotations in a more efficient way
        rotations = rotations % len(arr)
        arr = arr[-rotations:] + arr[:-rotations]

        # Find element at given index
        for r in ranges:
            arr = arr[r[0]:r[1] + 1]
        return arr[index]
    except Exception as e:
        return str(e)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()