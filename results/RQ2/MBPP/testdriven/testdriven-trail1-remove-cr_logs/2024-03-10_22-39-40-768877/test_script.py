def check_tuplex(tuplex, tuple1):
    if not isinstance(tuplex, tuple):
        return "Invalid input: 'tuplex' is not a tuple"
    try:
        if tuple1 in tuplex:
            return True
        else:
            return False
    except:
        return "Invalid input parameters"

# Test the function with an assertion
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
import unittest

class Test(unittest.TestCase):
    def test_check_tuplex(self):
        self.assertEqual(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r'), True)

if __name__ == '__main__':
    unittest.main()