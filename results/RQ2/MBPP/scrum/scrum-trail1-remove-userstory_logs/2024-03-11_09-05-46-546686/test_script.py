def text_match_two_three(text):
    import re  # Move the import statement for the re module outside of the function for better performance
    pattern = r'ab{2,3}'
    return bool(re.search(pattern, text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()