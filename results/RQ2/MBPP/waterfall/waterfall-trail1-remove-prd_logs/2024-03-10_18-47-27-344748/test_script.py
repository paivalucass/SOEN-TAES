def min_k(test_list, K):
    """
    This function returns the first K elements from the input list test_list, sorted based on the second element of each tuple in ascending order.
    If the input test_list is empty or if K is greater than the length of the list, it returns "Invalid input".
    """
    if not test_list or K > len(test_list):
        return "Invalid input"
    
    try:
        test_list.sort(key=lambda x: x[1])
        result = test_list[:K]
        return result
    except (TypeError, IndexError):
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test_min_k(self):
        self.assertEqual(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2), [('Akash', 2), ('Akshat', 4)])

if __name__ == '__main__':
    unittest.main()