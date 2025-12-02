def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    if not isinstance(sentence, str) or len(sentence) == 0:
        return "Invalid input"
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_words)
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(words_in_sentence('This is a test'), 'is')

    def test_example2(self):
        self.assertEqual(words_in_sentence('lets go for swimming'), 'go for')

if __name__ == '__main__':
    unittest.main()