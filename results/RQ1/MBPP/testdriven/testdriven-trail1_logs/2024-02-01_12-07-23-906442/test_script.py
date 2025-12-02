def long_words(n, input_str):
    if not input_str or not isinstance(n, int) or n <= 0:
        return "Invalid input"
    
    words = input_str.split()
    result = [word for word in words if len(word) > n]
    
    return list(set(result)) # To remove duplicates in the result list.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(long_words(3, "python is a programming language"), ['python', 'programming', 'language'])

if __name__ == '__main__':
    unittest.main()