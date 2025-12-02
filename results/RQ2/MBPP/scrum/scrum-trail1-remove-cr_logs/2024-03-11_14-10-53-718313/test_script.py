def find_Element(arr, ranges, rotations, index):
    n = len(arr)
    for r in ranges:
        left = r[0]
        right = r[1]
        arr[left:right+1] = arr[left:right+1][::-1]
    index = (index + rotations) % n
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test_find_element(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()