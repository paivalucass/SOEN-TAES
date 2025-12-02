def pack_consecutive_duplicates(list1):
    if not list1:  
        return []

    result = []
    sublist = []

    for item in list1:
        if not sublist or item != sublist[-1]: 
            if sublist:
                result.append(sublist)
                sublist = []
            sublist.append(item)
        else:
            sublist.append(item)

    if sublist:
        result.append(sublist)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()