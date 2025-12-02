def min_k(test_list, K):
    if not test_list:
        raise ValueError("Input list should not be empty")
    
    if K < 0 or K > len(test_list):
        raise ValueError("Value of K should be within the valid range")
    
    test_list.sort(key=lambda x: x[1])
    
    return test_list[:K]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2), [('Akash', 2), ('Akshat', 4)])

if __name__ == '__main__':
    unittest.main()