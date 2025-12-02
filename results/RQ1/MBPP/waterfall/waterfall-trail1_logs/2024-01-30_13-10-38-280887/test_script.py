def extract_nth_element(list1, n):
    if not isinstance(list1, list) or not list1:
        raise ValueError("Input is not a valid list or the list is empty")
    
    for item in list1:
        if not isinstance(item, tuple) or not item:
            raise ValueError("List contains non-tuple elements or the tuple is empty")

    if n < 0 or n >= len(list1[0]):
        raise ValueError("Invalid index value")

    result = [item[n] for item in list1]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()