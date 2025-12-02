def find_element(arr, ranges, rotations, index):
    for r in range(rotations):
        for start, end in ranges:
            arr[start:end + 1] = arr[start:end + 1][::-1]
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5], [[0,2],[0,3]], 2, 1), 3)

if __name__ == '__main__':
    unittest.main()