def check_tuplex(tuplex, element):
    if not isinstance(tuplex, tuple):
        raise TypeError("Expected a tuple for the first parameter")
    if element is None:
        raise ValueError("Element parameter cannot be None")

    return element in tuplex
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'), True)

if __name__ == '__main__':
    unittest.main()