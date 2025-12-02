def pack_consecutive_duplicates(list1):
    result = []
    current_sublist = []

    for index, element in enumerate(list1):
        if index == 0 or element != list1[index - 1]:
            if current_sublist:
                result.append(current_sublist)
            current_sublist = [element]
        else:
            current_sublist.append(element)

    if current_sublist:
        result.append(current_sublist)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()