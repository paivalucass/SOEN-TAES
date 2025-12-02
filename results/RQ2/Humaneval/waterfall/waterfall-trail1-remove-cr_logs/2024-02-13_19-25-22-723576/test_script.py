def by_length(arr):
    arr = [x for x in arr if 1 <= x <= 9]
    arr.sort()
    arr.reverse()
    replace_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    result = [replace_dict[x] for x in arr]
    return result
import unittest

class Test(unittest.TestCase):

    def test_by_length(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([1, -1, 55]), ["One"])

if __name__ == '__main__':
    unittest.main()