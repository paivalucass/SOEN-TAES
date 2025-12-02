def split(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    
    try:
        individual_characters_list = list(word)
        return individual_characters_list
    except Exception as e:
        raise Exception("An error occurred during the splitting process: " + str(e))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p', 'y', 't', 'h', 'o', 'n'])

if __name__ == '__main__':
    unittest.main()