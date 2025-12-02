def move_num(test_str):
    import re
    letters = ''.join(re.findall('[a-zA-Z]', test_str))
    numbers = ''.join(re.findall('[0-9]', test_str))
    return letters + numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()