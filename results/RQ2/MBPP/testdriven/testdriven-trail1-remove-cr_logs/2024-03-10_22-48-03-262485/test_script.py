def move_num(test_str):
    result = [char for char in test_str if not char.isdigit()]
    result.extend([char for char in test_str if char.isdigit()])
    return ''.join(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()