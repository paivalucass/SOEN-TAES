def long_words(n, input_str):
    if not isinstance(n, int) or not isinstance(input_str, str) or not input_str:
        return "Invalid input"
    
    word_list = input_str.split()
    
    result = [word for word in word_list if len(word) > n]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()