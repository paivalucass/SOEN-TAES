def pack_consecutive_duplicates(list1):
    result = []
    if not isinstance(list1, list):
        raise ValueError("Input is not a list")
    
    current_group = [list1[0]]
    for i in range(1, len(list1)):
        if list1[i] == list1[i-1]:
            current_group.append(list1[i])
        else:
            result.append(current_group)
            current_group = [list1[i]]
    
    result.append(current_group)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()