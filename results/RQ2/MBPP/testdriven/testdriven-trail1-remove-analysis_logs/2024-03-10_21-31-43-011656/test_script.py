def find_star_num(n): 
    ''' 
    Write a function to find the n'th star number. 
    assert find_star_num(3) == 37 
    '''
    # Input validation and edge case handling
    if type(n) != int or n < 0:
        return "Invalid Input"
    
    # Calculating the star number
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        star_number = 6*n**2 - 6*n + 1
        
        # Checking for integer limit
        if star_number > 2**31 - 1:
            return "Result exceeds integer limit"
        return star_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()