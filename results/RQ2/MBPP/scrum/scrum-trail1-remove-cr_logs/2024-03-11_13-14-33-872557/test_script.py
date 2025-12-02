def extract_nth_element(list1, n):
    if not list1:
        return "Error: Empty input list"
    if n < 0:
        return "Error: Negative index"
    if n >= len(list1[0]):
        return "Error: Index exceeds list length"

    return [item[n] for item in list1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0), ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'])

if __name__ == '__main__':
    unittest.main()