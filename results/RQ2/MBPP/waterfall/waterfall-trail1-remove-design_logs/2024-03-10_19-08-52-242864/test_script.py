def check_type(test_tuple):
    data_type = type(test_tuple[0])
    return all(type(element) == data_type for element in test_tuple)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()