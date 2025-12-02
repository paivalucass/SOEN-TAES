def move_num(test_str):
    import re
    if not test_str:
        return ""

    non_numeric_chars = ''.join(re.findall(r'\D', test_str))
    numeric_chars = ''.join(re.findall(r'\d', test_str))

    return non_numeric_chars + numeric_chars
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()