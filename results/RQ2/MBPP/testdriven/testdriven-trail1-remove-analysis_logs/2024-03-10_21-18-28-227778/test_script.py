def extract_nth_element(list_of_tuples, index):
    if not list_of_tuples:
        raise ValueError("Empty list: Unable to extract nth element")
    if index < 0:
        raise ValueError("Negative index: Unable to extract nth element")
    
    result = []
    for tuple in list_of_tuples:
        try:
            result.append(tuple[index])
        except IndexError:
            raise IndexError("Non-existent index: Unable to extract nth element")
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()