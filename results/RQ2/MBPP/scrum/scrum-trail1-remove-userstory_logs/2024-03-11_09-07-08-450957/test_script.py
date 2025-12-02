def colon_tuplex(tuplex, m, n):
    tup_list = list(tuplex)
    tup_list[2].append(n)
    return tuple(tup_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()