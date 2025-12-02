def replace_list(list1, list2):
    try:
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Invalid input")
        
        if not all(isinstance(x, (int, float)) for x in list1) or not all(isinstance(x, (int, float)) for x in list2):
            raise TypeError("Invalid input")
        
        if len(list1) == 0:
            return list2
        elif len(list2) == 0:
            return list1
        else:
            list1[-1:] = list2
            return list1
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]), [1, 3, 5, 7, 9, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()