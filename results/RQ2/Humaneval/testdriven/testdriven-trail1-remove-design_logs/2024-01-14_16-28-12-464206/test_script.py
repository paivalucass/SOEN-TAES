def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words) if prime_length_words else "Error: No prime length words found"
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(function_under_test('This is a test'), 'is')

    def test_example2(self):
        self.assertEqual(function_under_test('lets go for swimming'), 'go for')

if __name__ == '__main__':
    unittest.main()