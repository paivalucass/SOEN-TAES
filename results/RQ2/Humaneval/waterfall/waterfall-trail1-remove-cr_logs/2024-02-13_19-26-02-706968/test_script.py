def histogram(test):
    letters = test.split()
    letter_count = {}
    
    for letter in letters:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    
    if not letter_count:
        return {}
    
    max_count = max(letter_count.values())
    max_letters = [letter for letter, count in letter_count.items() if count == max_count]
    
    return {letter: count for letter, count in letter_count.items() if count == max_count}
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