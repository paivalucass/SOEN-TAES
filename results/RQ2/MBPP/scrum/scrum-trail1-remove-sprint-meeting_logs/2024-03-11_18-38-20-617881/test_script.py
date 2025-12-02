def colon_tuplex(tuplex, m, n):
    lst = list(tuplex)
    lst[m] = [n]
    return tuple(lst)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()