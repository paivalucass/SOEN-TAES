def count_samepair(list1, list2, list3):
    identical_count = 0
    for i in range(min(len(list1), len(list2), len(list3))):
        if list1[i] == list2[i] == list3[i]:
            identical_count += 1
    return identical_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]), 3)

if __name__ == '__main__':
    unittest.main()