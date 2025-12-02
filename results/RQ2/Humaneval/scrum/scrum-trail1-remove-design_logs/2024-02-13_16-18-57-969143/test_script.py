from collections import defaultdict

def histogram(test):
    if not test:
        return {}

    counts = defaultdict(int)
    test = test.replace(" ", "")
    for char in test:
        counts[char] += 1

    max_count = max(counts.values())
    result = {char: count for char, count in counts.items() if count == max_count}

    return result
import unittest

class Test(unittest.TestCase):
    def test_histogram(self):
        self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('b b b b a'), {'b': 4})
        self.assertEqual(histogram(''), {})

if __name__ == '__main__':
    unittest.main()