def is_sublist(main_list, sublist):
    if not isinstance(main_list, list) or not isinstance(sublist, list):
        raise TypeError("Both main_list and sublist should be of type list")
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test_is_sublist(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[3,7]), True)
        self.assertEqual(is_sublist([2,4,3,5,7],[3,8]), False)

if __name__ == '__main__':
    unittest.main()