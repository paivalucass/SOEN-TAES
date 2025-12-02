def count_samepair(list1, list2, list3):
    '''Write a function to count the number of items that are identical in the same position of three given lists.'''
    
    if len(list1) == 0 or len(list2) == 0 or len(list3) == 0:
        return "Invalid input"
    
    if len(list1) != len(list2) or len(list2) != len(list3):
        return "Invalid input"
    
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] and list2[i] == list3[i]:
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]), 3)

if __name__ == '__main__':
    unittest.main()