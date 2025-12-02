def check_value(dictionary, n):
    if not isinstance(dictionary, dict):
        raise TypeError("Input is not a dictionary")
    if not dictionary:
        raise ValueError("Input dictionary is empty")
    if not all(value == list(dictionary.values())[0] for value in dictionary.values()):
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), True)

if __name__ == '__main__':
    unittest.main()