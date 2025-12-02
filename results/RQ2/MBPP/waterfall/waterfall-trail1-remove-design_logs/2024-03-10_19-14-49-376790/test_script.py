def overlapping(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1.intersection(set2)) > 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(overlapping([1,2,3,4,5],[6,7,8,9]), False)

if __name__ == '__main__':
    unittest.main()