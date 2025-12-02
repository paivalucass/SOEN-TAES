def words_in_sentence(sentence):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def words_with_prime_length(sentence):
        words = sentence.split()
        prime_length_words = []
        for word in words:
            if is_prime(len(word)):
                prime_length_words.append(word)
        return ' '.join(prime_length_words)
    
    return words_with_prime_length(sentence)
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(words_in_sentence('This is a test'), 'is')

    def test_example2(self):
        self.assertEqual(words_in_sentence('lets go for swimming'), 'go for')

if __name__ == '__main__':
    unittest.main()