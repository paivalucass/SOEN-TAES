def check_tuplex(tuplex, element):
    if not isinstance(tuplex, tuple) or len(tuplex) == 0:
        raise ValueError("Input tuple is not valid")

    return element in tuplex
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'))

if __name__ == '__main__':
    unittest.main()