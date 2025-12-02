def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(overlapping([1,2,3,4,5],[6,7,8,9]), False)

if __name__ == '__main__':
    unittest.main()