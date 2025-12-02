def extract_nth_element(list1, n):
    if not isinstance(list1, list):
        raise TypeError("Error: Input is not a list")
        
    if not list1:
        raise ValueError("Error: Empty list provided")
    
    if any(len(tup) < n + 1 for tup in list1):
        raise ValueError("Error: Tuple length does not match")
    
    if n < 0 or n >= len(list1[0]):
        raise ValueError("Error: Value of n is out of range")
    
    return [tup[n] for tup in list1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()