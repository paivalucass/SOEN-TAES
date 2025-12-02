def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def words_in_sentence(sentence):
    if not sentence:
        return ""
    
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_length_words)

import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(words_in_sentence('This is a test'), 'is')

    def test_example2(self):
        self.assertEqual(words_in_sentence('lets go for swimming'), 'go for')

if __name__ == '__main__':
    unittest.main()