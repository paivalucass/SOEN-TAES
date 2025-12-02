FIX = """"""
def vowels_count(s):
    """
    Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    count = 0

    # Use regular expressions to check if the input string contains unexpected characters
    if not isinstance(s, str) or re.search('[^a-zA-ZyY]', s) or len(s) > 100:
        raise ValueError('Unexpected input')

    # Iterate over each letter in the word and count the number of vowels
    for letter in s:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y' if s[-1] == 'y' else '']:
            count += 1

    return count
import unittest

class Test(unittest.TestCase):

    def test_vowels_count(self):
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        self.assertEqual(vowels_count('Hello World'), 3)
        self.assertEqual(vowels_count('Python'), 1)
        self.assertEqual(vowels_count(''), 0)

if __name__ == '__main__':
    unittest.main()