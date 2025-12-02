def remove_elements(list1, list2):
    set2 = set(list2)
    result = [x for x in list1 if x not in set2]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]), [1, 3, 5, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()