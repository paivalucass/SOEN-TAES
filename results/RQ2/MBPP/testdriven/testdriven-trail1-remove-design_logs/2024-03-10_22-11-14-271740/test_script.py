def Find_Max_Length(lst):
    try:
        if not isinstance(lst, list) or any(not isinstance(sub_lst, list) for sub_lst in lst):
            raise ValueError("Invalid input")
        
        max_length = 0
        for sub_lst in lst:
            max_length = max(max_length, len(sub_lst))
        
        return max_length
    except Exception as e:
        raise ValueError("An error occurred: " + str(e)) from e
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max_Length([[1],[1,4],[5,6,7,8]]), 4)

if __name__ == '__main__':
    unittest.main()