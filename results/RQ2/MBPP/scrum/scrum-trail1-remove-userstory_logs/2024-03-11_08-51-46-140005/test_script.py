def is_sublist(main_list, sublist):
    if not isinstance(main_list, list) or not isinstance(sublist, list):
        return "Invalid input"
    if len(sublist) == 0:
        return False
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sublist([2,4,3,5,7], [3,7]), False)

if __name__ == '__main__':
    unittest.main()