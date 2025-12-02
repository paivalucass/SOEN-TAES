def find_element(arr, ranges, rotations, index):
    def rotate_subarray(subarr, rot):
        rot = rot % len(subarr)
        return subarr[-rot:] + subarr[:-rot]
    for r in ranges:
        start, end = r[0], r[1]
        subarr = arr[start:end+1]
        arr[start:end+1] = rotate_subarray(subarr, rotations)
    return arr[index] if index < len(arr) else None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()