def list_split(S, step):
    from itertools import zip_longest
    result = [S[i:i+step] for i in range(0, len(S), step)]
    return [list(x) for x in zip_longest(*result, fillvalue='')]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()