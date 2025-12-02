def find_Element(arr, ranges, rotations, index):
    for r in ranges:
        left = r[0]
        right = r[1]
        for i in range(rotations):
            temp = arr[right]
            for j in range(right, left, -1):
                arr[j] = arr[j-1]
            arr[left] = temp
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()