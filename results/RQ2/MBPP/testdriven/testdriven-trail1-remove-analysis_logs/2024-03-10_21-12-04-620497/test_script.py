def remove_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both list1 and list2 must be of type list")

    return [x for x in list1 if x not in list2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]), [1, 3, 5, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()