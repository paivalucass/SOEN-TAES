def colon_tuplex(tuplex, m, n):
    try:
        if not isinstance(tuplex, tuple):
            raise TypeError("Input data is not a tuple")
        
        if m < 0 or m >= len(tuplex):
            return tuplex
        
        new_tuplex = list(tuplex)
        new_tuplex[m] = n
        if isinstance(tuplex[m], list):
            new_tuplex[m] = [n]
        return tuple(new_tuplex)
    except TypeError as e:
        return e
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()