def check_tuplex(tuplex, element):
    if isinstance(tuplex, tuple):
        if element in tuplex:
            return True
        else:
            return False
    else:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'))

if __name__ == '__main__':
    unittest.main()