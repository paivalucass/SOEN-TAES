def histogram(test):
    letter_count = {}
    max_count = 1
    
    if not test: 
        return letter_count
    
    for letter in test.split():
        if letter in letter_count:
            letter_count[letter] += 1
            if letter_count[letter] > max_count:
                max_count = letter_count[letter]
        else:
            letter_count[letter] = 1
    
    result = {key: value for key, value in letter_count.items() if value == max_count}
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