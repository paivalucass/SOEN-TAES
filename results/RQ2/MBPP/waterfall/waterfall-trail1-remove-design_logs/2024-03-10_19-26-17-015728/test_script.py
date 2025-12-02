def pack_consecutive_duplicates(list1):
    packed_list = []
    i = 0
    while i < len(list1):
        current_value = list1[i]
        count = 1
        while (i + 1) < len(list1) and list1[i + 1] == current_value:
            count += 1
            i += 1
        sublist = [current_value] * count
        packed_list.append(sublist)
        i += 1
    return packed_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()