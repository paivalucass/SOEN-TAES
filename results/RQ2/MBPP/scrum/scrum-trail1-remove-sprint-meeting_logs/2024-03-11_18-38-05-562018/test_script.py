def find_Element(arr, ranges, rotations, index):
    for r in ranges:
        start = r[0]
        end = r[1]
        for i in range(rotations):
            temp = arr[end]
            for j in range(end, start, -1):
                arr[j] = arr[j-1]
            arr[start] = temp
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()