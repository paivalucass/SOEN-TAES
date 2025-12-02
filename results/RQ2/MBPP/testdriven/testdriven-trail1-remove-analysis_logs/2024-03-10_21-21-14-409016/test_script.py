def check_value(dictionary, n):
    if not isinstance(dictionary, dict):
        raise TypeError("Input is not a dictionary")

    if not dictionary:
        return True

    first_value = next(iter(dictionary.values()))
    for value in dictionary.values():
        if value != first_value:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_value(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()