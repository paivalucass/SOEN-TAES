def move_num(test_str):
    letters = ""
    numbers = ""
    special_chars = ""
    for char in test_str:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
        else:
            special_chars += char
    return letters + special_chars + numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()