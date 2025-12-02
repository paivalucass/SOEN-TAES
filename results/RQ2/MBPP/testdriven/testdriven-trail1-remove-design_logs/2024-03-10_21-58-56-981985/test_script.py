def long_words(n, input_str):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(input_str, str):
        raise ValueError("input_str must be a string")

    words = input_str.split()
    result = [word for word in words if len(word) > n]
    return result
import unittest

class Test(unittest.TestCase):
    def test_long_words(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()