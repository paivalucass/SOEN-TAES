def histogram(test):
    result = {}
    letters = test.split()
    
    for letter in letters:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    
    if result:
        max_count = max(result.values())
        max_letters = [letter for letter, count in result.items() if count == max_count]
        return {letter: count for letter, count in result.items() if count == max_count or letter in max_letters}
    else:
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