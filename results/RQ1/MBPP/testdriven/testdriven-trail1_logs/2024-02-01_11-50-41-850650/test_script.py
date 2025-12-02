def test_duplicate(arraynums):
    '''Write a function to find whether a given array of integers contains any duplicate element.'''
    
    if len(arraynums) == 0 or len(arraynums) == 1:
        return False
    
    num_set = set()
    for num in arraynums:
        if num in num_set:
            return True
        else:
            num_set.add(num)
    
    return False

# Example test case
assert test_duplicate([1,2,3,4,5])==False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()