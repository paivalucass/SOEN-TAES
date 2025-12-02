def find_Element(arr, ranges, rotations, index):
    for r in ranges:
        start, end = r
        section1 = arr[:start]
        section2 = arr[start:end]
        section3 = arr[end:]
        arr = section3 + section1 + section2
    return arr[index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1), 3)

if __name__ == '__main__':
    unittest.main()