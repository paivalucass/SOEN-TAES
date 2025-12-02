def check_value(dictionary: dict, value) -> bool:
    if not dictionary:
        return False
    for val in dictionary.values():
        if val != value:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()