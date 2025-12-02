def find_element(arr, ranges, rotations, index):
    temp = arr[:]
    for r in ranges:
        start_index = r[0]
        end_index = r[1]
        length = len(arr)
        rotate = rotations % length
        for i in range(rotate):
            for j in range(start_index, end_index+1):
                arr[j] = temp[(j-1+length) % length]
            temp = arr[:]
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()