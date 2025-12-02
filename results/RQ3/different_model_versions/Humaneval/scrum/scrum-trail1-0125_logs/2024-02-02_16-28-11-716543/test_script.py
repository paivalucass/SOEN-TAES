def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    if not sentence:
        return ""

    def is_prime_length(word):
        return is_prime_number(len(word))

    prime_words = [word for word in sentence.split() if is_prime_length(word)]
    return " ".join(prime_words) if prime_words else "" 

# Unit Test
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
print(words_in_sentence(""))  # Output: ""
print(words_in_sentence("a bc def"))  # Output: "bc def"
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(words_in_sentence('This is a test'), 'is')

    def test_example2(self):
        self.assertEqual(words_in_sentence('lets go for swimming'), 'go for')

if __name__ == '__main__':
    unittest.main()