def combinations_colors(l, n):
    result = []
    if n == 1:
        for i in range(len(l)):
            result.append((l[i],))
    else:
        for i in range(len(l)):
            for item in combinations_colors(l, n-1):
                result.append((l[i],) + item)
    return result
import unittest

class Test(unittest.TestCase):
    def test_combinations_colors(self):
        self.assertEqual(combinations_colors(['Red', 'Green', 'Blue'], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()