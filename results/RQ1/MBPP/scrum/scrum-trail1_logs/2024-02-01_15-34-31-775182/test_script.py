def extract_nth_element(list1, n):
    if not all(isinstance(item, tuple) for item in list1):
        raise ValueError("list1 must contain only tuples")
    if not all(0 <= n < len(item) for item in list1):
        raise ValueError("index n is out of bounds in at least one tuple in list1")

    extracted_elements = [item[n] for item in list1]
    return extracted_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()