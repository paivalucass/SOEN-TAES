def issort_list(list1):
    if list1 == []:
        return []
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(issort_list([1,2,4,6,8,10,12,14,16,17]), True)

if __name__ == '__main__':
    unittest.main()