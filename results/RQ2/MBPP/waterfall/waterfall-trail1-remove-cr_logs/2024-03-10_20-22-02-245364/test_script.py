def remove_kth_element(list1, k):
    try:
        if len(list1) == 0:
            raise ValueError("Error: Empty list")
        elif k < 0 or k >= len(list1):
            raise ValueError("Error: K out of range")
        
        new_list = list1[:k] + list1[k+1:]
        return new_list
    
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test_remove_kth_element(self):
        self.assertEqual(remove_kth_element([1,1,2,3,4,4,5,1], 3), [1, 1, 3, 4, 4, 5, 1])

if __name__ == '__main__':
    unittest.main()