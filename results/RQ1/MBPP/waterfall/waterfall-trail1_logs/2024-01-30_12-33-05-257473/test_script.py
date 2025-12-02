def string_to_list(string):
    try:
        if not string:
            raise ValueError("Input string is empty")
        word_list = string.split(' ')
        return word_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()