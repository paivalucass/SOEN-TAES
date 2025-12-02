def check_tuplex(tuplex, tuple1):
    if not isinstance(tuplex, tuple) or not isinstance(tuple1, tuple):
        return "Error: Input is not a tuple"

    if tuple1 in tuplex:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'))

if __name__ == '__main__':
    unittest.main()