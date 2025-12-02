def by_length(arr):
    arr = [x for x in arr if 1 <= x <= 9]
    arr.sort()
    arr.reverse()
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = [digit_names[x-1] for x in arr]
    return result
import unittest

class Test(unittest.TestCase):
    def test_by_length(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([1, -1 , 55]), ["One"])

if __name__ == '__main__':
    unittest.main()