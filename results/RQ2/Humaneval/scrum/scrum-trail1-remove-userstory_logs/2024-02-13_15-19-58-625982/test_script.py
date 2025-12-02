def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    from collections import defaultdict
    if not isinstance(test, str):
        raise TypeError("Input should be a string")

    # Create a defaultdict to track letter occurrences
    letter_counts = defaultdict(int)

    # Handle edge case for empty input strings
    if not test:
        return {}

    # Update letter counts
    for letter in test:
        if letter.isalpha():
            letter_counts[letter] += 1

    # Find the maximum occurrence
    max_count = max(letter_counts.values())

    # Create a dictionary to store letters with the maximum occurrence
    result = {letter: count for letter, count in letter_counts.items() if count == max_count}

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