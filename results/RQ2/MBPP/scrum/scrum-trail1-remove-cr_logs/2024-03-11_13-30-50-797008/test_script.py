def Find_Max_Length(lst):
    max_length = 0
    if isinstance(lst, list):
        for sub_list in lst:
            if isinstance(sub_list, list):
                if len(sub_list) > max_length:
                    max_length = len(sub_list)
            else:
                return "Error"
        return max_length
    else:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()