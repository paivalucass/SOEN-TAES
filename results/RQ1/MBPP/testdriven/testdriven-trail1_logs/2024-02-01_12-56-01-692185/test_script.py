def extract_values(text):
    '''Write a function to extract values between quotation marks from a string.'''
    import re
    quoted_values = re.findall(r'\"(.*?)\"', text)
    return quoted_values

assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()