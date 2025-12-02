def extract_nth_element(list1, n):
    if not list1 or not all(isinstance(item, tuple) for item in list1):
        raise ValueError("Input list is empty or contains elements that are not tuples.")
    if any(n >= len(item) for item in list1):
        raise ValueError("Index n is out of range for the tuples in the list.")
    return [item[n] for item in list1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()