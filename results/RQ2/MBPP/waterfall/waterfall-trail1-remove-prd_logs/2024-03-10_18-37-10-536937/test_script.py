def extract_nth_element(list1, n):
    if not isinstance(list1, list):
        return "Input is not a list"
    if not list1:
        return "List is empty"
    if not all(isinstance(x, tuple) for x in list1):
        return "Input is not a list of tuples"
    if n < 0 or n >= len(list1[0]):
        return "Invalid index"

    return [x[n] for x in list1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()