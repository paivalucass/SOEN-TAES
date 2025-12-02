def move_num(test_str):
    letters = [char for char in test_str if not char.isdigit()]
    numbers = [char for char in test_str if char.isdigit()]
    return ''.join(letters + numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()