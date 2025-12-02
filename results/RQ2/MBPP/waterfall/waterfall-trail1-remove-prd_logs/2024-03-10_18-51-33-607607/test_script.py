def find_element(arr, ranges, rotations, index):
    if len(arr) == 0 or rotations < 0 or index < 0:
        return "Error: Invalid input"

    array_length = len(arr)
    for r in ranges:
        start, end = r
        start = start % array_length
        end = end % array_length
        if start <= end:
            arr = arr[:start] + arr[end+1:] + arr[start:end+1]
        else:
            arr = arr[end+1:start] + arr[start:end+1]

    if index >= array_length:
        return "Error: Index out of range"
    else:
        return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()