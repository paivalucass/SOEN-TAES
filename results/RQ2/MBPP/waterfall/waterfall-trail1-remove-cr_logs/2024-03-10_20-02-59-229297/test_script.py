def check_tuplex(tuplex, element):
    if not isinstance(tuplex, tuple) or len(tuplex) == 0:
        raise ValueError("Input tuple is empty or not a tuple")

    if type(element) not in map(type, tuplex):
        raise TypeError("Element to be checked is not of the same type as the elements in the tuple")

    if element in tuplex:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), "r"), True)

if __name__ == '__main__':
    unittest.main()