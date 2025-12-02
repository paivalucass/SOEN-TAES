def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    if not sentence:
        return "Input sentence is empty"
    
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    
    if not prime_length_words:
        return "No prime length words found in the input sentence"

    return ' '.join(prime_length_words)
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(words_in_sentence('This is a test'), 'is')

    def test_example2(self):
        self.assertEqual(words_in_sentence('lets go for swimming'), 'go for')

if __name__ == '__main__':
    unittest.main()