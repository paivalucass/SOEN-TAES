def pack_consecutive_duplicates(list1):
    if not list1:
        return []
    
    result = []
    temp = [list1[0]]
    
    for i in range(1, len(list1)):
        if list1[i] == list1[i-1]:
            temp.append(list1[i])
        else:
            result.append(temp)
            temp = [list1[i]]
    
    result.append(temp)
    
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), 
                         [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]])

if __name__ == '__main__':
    unittest.main()