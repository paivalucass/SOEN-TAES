def long_words(n, word_list):
    return [word for word in word_list.split() if len(word) > n]

# Test cases
print(long_words(3, 'python is a programming language'))  # ['python', 'programming', 'language']
print(long_words(5, 'apple banana orange grape kiwi'))  # ['banana', 'orange']
print(long_words(4, ''))  # []
print(long_words(3, '@python is a programming@ language'))  # ['@python', 'programming@', 'language']
print(long_words(4, 'apple banana banana orange  grape kiwi'))  # ['banana', 'banana', 'orange', 'grape']
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()