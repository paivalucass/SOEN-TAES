def colon_tuplex(tuplex, m, n):
    if not isinstance(tuplex, tuple):
        raise ValueError("Input 'tuplex' should be a tuple")
    if not isinstance(m, int):
        raise ValueError("Input 'm' should be an integer")
    if m < 0 or m > len(tuplex):
        raise ValueError("Position 'm' is out of range")
    new_list = list(tuplex)
    new_list.insert(m, n)
    result_tuple = tuple(new_list)
    return result_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()