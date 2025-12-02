def by_length(arr):
    mapping = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    valid_integers = [x for x in arr if isinstance(x, int) and 1 <= x <= 9]

    sorted_integers = sorted(valid_integers, key=lambda x: -x)

    result = [mapping[x] for x in sorted_integers]

    return result
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])

    def test2(self):
        self.assertEqual(by_length([]), [])

    def test3(self):
        self.assertEqual(by_length([1, -1, 55]), ['One'])

if __name__ == '__main__':
    unittest.main()