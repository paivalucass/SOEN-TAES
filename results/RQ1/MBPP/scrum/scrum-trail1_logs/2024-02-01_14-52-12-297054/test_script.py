def check_type(test_tuple):
    if not isinstance(test_tuple, tuple):
        raise TypeError("Input should be a tuple")

    data_type = type(test_tuple[0])

    for element in test_tuple:
        if not isinstance(element, data_type):
            return False

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()