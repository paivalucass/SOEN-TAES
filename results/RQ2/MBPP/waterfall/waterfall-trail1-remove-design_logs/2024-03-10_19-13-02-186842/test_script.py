def colon_tuplex(tuplex, m, n):
    if m < 0 or m >= len(tuplex):
        raise ValueError("Index m is out of bounds")
    
    new_tuplex = list(tuplex)
    if isinstance(new_tuplex[m], list):
        new_tuplex[m].append(n)
    else:
        new_tuplex[m] = [n]
    return tuple(new_tuplex)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()