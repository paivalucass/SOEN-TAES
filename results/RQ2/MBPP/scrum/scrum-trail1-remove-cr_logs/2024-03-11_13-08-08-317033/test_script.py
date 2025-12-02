def find_Element(arr, ranges, rotations, index):
    for i in range(rotations):
        a = arr.pop(0)
        arr.append(a)
    result = arr[index]
    for r in ranges:
        start = r[0]
        end = r[1]
        result = arr[start:end+1][index]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()