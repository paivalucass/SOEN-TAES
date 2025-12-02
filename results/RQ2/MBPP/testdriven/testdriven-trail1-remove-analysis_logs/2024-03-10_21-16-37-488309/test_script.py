def colon_tuplex(tuplex, m, n):
    if not isinstance(tuplex, tuple):
        raise TypeError("Input is not a tuple error")
    if m < 0 or m > len(tuplex) + 1:
        raise ValueError("Index out of range error")

    tuplex_list = list(tuplex)
    tuplex_list.insert(m, n)
    return tuple(tuplex_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()