def move_num(test_str):
    alpha_chars = []
    num_chars = []

    for char in test_str:
        if char.isnumeric():
            num_chars.append(char)
        elif char.isalpha():
            alpha_chars.append(char)

    return ''.join(alpha_chars) + ''.join(num_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()