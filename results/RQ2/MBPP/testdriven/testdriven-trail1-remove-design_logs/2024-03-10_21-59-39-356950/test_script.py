def count_samepair(list1, list2, list3):
    if len(list1) != len(list2) or len(list2) != len(list3):
        return "Error: Input lists are not of the same length"
    
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_samepair(self):
        self.assertEqual(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]), 3)

if __name__ == '__main__':
    unittest.main()