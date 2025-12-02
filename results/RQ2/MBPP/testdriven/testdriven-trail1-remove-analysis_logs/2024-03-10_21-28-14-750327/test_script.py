def capital_words_spaces(str1):
    result = ""
    for i in range(len(str1)):
        if str1[i].istitle() and i != 0:
            result += " " + str1[i]
        else:
            result += str1[i]
    return result

assert capital_words_spaces("Python") == 'Python'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()