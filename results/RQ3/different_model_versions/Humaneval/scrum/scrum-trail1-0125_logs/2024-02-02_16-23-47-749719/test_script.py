def histogram(test):
    histogram_dict = {}
    if test:
        letters = test.split()
        for letter in letters:
            if letter in histogram_dict:
                histogram_dict[letter] += 1
            else:
                histogram_dict[letter] = 1
        max_count = max(histogram_dict.values()) if histogram_dict else 0
        return {key: value for key, value in histogram_dict.items() if value == max_count}
    return {}
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