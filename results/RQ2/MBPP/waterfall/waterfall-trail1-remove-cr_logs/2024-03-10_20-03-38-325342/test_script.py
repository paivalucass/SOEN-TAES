def extract_nth_element(list1, n):
    if not list1:
        raise ValueError("Input list of tuples cannot be empty")
    if any(n < 0 or n >= len(item) for item in list1):
        raise ValueError("Index out of range")
    result = [item[n] for item in list1]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()