def histogram(test):
    if not test:
        return {}
    test_list = test.split()
    hist_dict = {}
    for letter in test_list:
        if letter in hist_dict:
            hist_dict[letter] += 1
        else:
            hist_dict[letter] = 1
    max_count = max(hist_dict.values())
    result = {key: value for key, value in hist_dict.items() if value == max_count}
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