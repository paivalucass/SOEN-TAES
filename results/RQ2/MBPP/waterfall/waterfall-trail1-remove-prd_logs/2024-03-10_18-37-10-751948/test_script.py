def overlapping(list1, list2):
    if not list1 or not list2:
        return False
    else:
        for value in list1:
            if value in list2:
                return True
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(overlapping([1,2,3,4,5],[6,7,8,9]), False)

if __name__ == '__main__':
    unittest.main()