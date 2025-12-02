def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_word_length(word):
    return len(word)

def words_in_sentence(sentence):
    if sentence is None or len(sentence) == 0:
        return ""

    result = []
    words = sentence.split(" ")
    for word in words:
        if is_prime(get_word_length(word)):
            result.append(word)

    return " ".join(result)
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(words_in_sentence('This is a test'), 'is')

    def test_example2(self):
        self.assertEqual(words_in_sentence('lets go for swimming'), 'go for')

if __name__ == '__main__':
    unittest.main()