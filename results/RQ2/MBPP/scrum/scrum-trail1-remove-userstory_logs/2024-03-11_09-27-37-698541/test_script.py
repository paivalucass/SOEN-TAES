def pack_consecutive_duplicates(list1):
    result = []
    current_sequence = []

    for i in range(len(list1)):
        if i == 0 or list1[i] != list1[i-1]:
            if current_sequence:
                result.append(current_sequence)
                current_sequence = []
        current_sequence.append(list1[i])

    if current_sequence:
        result.append(current_sequence)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()