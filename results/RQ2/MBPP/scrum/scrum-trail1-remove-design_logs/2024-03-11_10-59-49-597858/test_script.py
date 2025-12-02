def move_num(test_str):
    import re
    numbers = re.findall("\d+", test_str)
    non_numbers = re.sub("\d+", "", test_str)
    return non_numbers + "".join(numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()