def check_tuplex(tuplex, tuple1):
    return tuple1 in tuplex
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), "r"))

if __name__ == '__main__':
    unittest.main()