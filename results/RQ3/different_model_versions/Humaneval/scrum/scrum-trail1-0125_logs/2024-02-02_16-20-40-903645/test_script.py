def add(lst):
    """
    Given a non-empty list of integers lst. add the even elements that are at odd indices..
    
    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst or len(lst) < 2:
        return 0
    
    sum_even_elements = 0

    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            sum_even_elements += lst[i]

    return sum_even_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()