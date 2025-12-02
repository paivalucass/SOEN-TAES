def issort_list(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input is not a list")
    
    if len(input_list) < 2:
        return True
    
    for i in range(len(input_list) - 1):
        if input_list[i] > input_list[i+1]:
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test_issort_list(self):
        self.assertTrue(issort_list([1,2,4,6,8,10,12,14,16,17]))

if __name__ == '__main__':
    unittest.main()