def find_element(arr, ranges, rotations, index):
    if len(arr) == 0:
        return "Error: Input Array is empty"
    if rotations < 0:
        return "Error: Negative rotations not allowed"
    if index >= len(arr):
        return "Error: Index out of bounds"
    
    for i in range(rotations % len(arr)):
        temp = arr.pop()
        arr.insert(0, temp)
    
    for r in ranges:
        start = r[0]
        end = r[1]
        if end >= len(arr):
            return "Error: Range out of bounds"
        sub_arr = arr[start:end+1]
        if index >= start and index <= end:
            return arr[index]
    return "Error: Index out of bounds"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()