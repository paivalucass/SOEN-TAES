def extract_nth_element(list1, n):
    if not isinstance(list1, list) or not all(isinstance(item, tuple) for item in list1):
        raise ValueError("Input should be a list of tuples")
        
    result = [item[n] if len(item) > n else "Error: Index out of range" for item in list1]
    
    if len(list1) == 0:
        result = "Error: Empty list"
    elif len(set(len(item) for item in list1)) != 1:
        result = "Error: Tuples have different lengths"
    
    return result

# Test the function
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0) == ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0),['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()