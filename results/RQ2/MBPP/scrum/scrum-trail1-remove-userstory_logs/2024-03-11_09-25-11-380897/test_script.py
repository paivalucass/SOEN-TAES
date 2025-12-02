def capital_words_spaces(str1):
    new_str = ""
    for i in range(len(str1)):
        if i > 0 and str1[i].isupper():
            new_str += " " + str1[i]
        else:
            new_str += str1[i]
    return new_str

# Additional test cases
print(capital_words_spaces("HelloWorld"))  # Output: "Hello World"
print(capital_words_spaces("ThisIsATest"))  # Output: "This Is A Test"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()