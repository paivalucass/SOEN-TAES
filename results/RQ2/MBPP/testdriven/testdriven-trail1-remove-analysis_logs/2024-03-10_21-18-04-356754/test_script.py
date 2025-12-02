def check_tuplex(tuplex, element):
    if not isinstance(tuplex, tuple) or not isinstance(element, (str, int)):
        raise Exception("Invalid input: The input should be a tuple and the element should be a string or an integer")
    return element in tuplex
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'), True)

if __name__ == '__main__':
    unittest.main()