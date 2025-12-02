def pack_consecutive_duplicates(list1):
    result = []
    i = 0
    while i < len(list1):
        current = [list1[i]]
        while i < len(list1) - 1 and list1[i] == list1[i + 1]:
            current.append(list1[i + 1])
            i += 1
        result.append(current)
        i += 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()