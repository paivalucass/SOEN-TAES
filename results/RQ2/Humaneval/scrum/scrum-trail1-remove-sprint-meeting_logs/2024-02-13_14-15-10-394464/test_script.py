def by_length(arr):
    result = []
    digit_names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    sorted_arr = sorted([x for x in arr if 0 < x < 10])
    sorted_arr.reverse()
    for num in sorted_arr:
        result.append(digit_names[num])
    return result
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])

    def test_2(self):
        self.assertEqual(by_length([]), [])

    def test_3(self):
        self.assertEqual(by_length([1, -1, 55]), ["One"])

if __name__ == '__main__':
    unittest.main()