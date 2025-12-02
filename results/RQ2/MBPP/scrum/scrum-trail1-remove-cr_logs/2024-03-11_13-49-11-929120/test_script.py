def move_num(test_str):
    letters = ''
    numbers = ''
    for char in test_str:
        if char.isdigit():
            numbers += char
        else:
            letters += char
    return letters + numbers
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()