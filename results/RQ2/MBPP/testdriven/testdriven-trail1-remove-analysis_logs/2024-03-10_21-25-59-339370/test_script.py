def replace_spaces(text):
    modified_chars = []
    for char in text:
        if char == " ":
            modified_chars.append("_")
        elif char == "_":
            modified_chars.append(" ")
        else:
            modified_chars.append(char)
    return "".join(modified_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()