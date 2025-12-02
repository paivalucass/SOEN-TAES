def colon_tuplex(tuplex, index, value):
    if index < 0 or index >= len(tuplex):
        return tuplex
    else:
        new_tuplex = list(tuplex)
        new_tuplex[index] = value
        return tuple(new_tuplex)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()