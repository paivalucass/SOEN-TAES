def check_tuplex(tuplex, element):
    return element in tuplex
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'), True)

if __name__ == '__main__':
    unittest.main()