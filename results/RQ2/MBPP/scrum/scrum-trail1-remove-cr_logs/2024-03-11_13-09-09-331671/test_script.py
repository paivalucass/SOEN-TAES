def colon_tuplex(tuplex, m, n):
    if not isinstance(m, int) or m < 0 or m >= len(tuplex) or not isinstance(n, (int, str, bool, list)):
        return "Error: Invalid index or value input"
    modified_tuple = list(tuplex)
    if not modified_tuple[m]:
        modified_tuple[m] = [n]
    else:
        modified_tuple[m].append(n)
    return tuple(modified_tuple)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()