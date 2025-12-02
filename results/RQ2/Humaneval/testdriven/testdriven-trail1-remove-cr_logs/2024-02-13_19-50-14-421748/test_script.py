def histogram(test):
    result = {}
    if len(test) == 0:
        return result

    test = test.split()
    for letter in test:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    max_count = max(result.values())
    max_letters = [letter for letter, count in result.items() if count == max_count]

    return {letter: max_count for letter in max_letters}
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