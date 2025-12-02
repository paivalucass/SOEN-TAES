def rear_extract(test_list):
    result_list = []
    if test_list is None:
        return "Error: Null input list"
    if not isinstance(test_list, list):
        return "Error: Invalid input list"
    for tup in test_list:
        if not isinstance(tup, tuple):
            return "Error: Invalid input list"
        result_list.append(tup[-1])
    return result_list
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()