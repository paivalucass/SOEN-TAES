def anti_shuffle(s):
    if not s:
        return s  # Return the input string if it is empty
    elif not s.strip():
        return s  # Return the input string if it only contains spaces
    else:
        words = s.split()  # Split the input string into words
        result = []
        for word in words:
            sorted_word = ''.join(sorted(word))  # Sort the characters of each word
            result.append(sorted_word)
        return ' '.join(result)  # Join the sorted words with spaces and return the result

import unittest

class Test(unittest.TestCase):
    def test_anti_shuffle(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()