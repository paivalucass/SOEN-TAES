def add(lst):
    """
    Given a non-empty list of integers lst. add the even elements that are at odd indices..
    
    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Input validation
    if not isinstance(lst, list) or len(lst) == 0:
        return "Invalid input. Please provide a non-empty list of integers."
    
    # Initialize sum
    total_sum = 0
    
    # Iterate through the list and add even elements at odd indices to the sum
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total_sum += lst[i]
    
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()