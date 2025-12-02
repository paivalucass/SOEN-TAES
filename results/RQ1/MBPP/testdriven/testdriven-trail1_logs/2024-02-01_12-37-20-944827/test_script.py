def check_tuplex(tuplex, element):
    if not isinstance(tuplex, tuple):
        raise TypeError("tuplex should be a tuple")
    if not isinstance(element, (int, str, float)):
        raise TypeError("element should be of type int, str, or float")

    return element in tuplex
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'), True)

if __name__ == '__main__':
    unittest.main()