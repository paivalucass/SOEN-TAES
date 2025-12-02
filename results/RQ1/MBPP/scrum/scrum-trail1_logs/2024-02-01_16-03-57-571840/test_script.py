import re

def extract_values(text):
    pattern = r'\"(.*?)\"'
    values = re.findall(pattern, text)
    
    if not values:
        raise ValueError("No values found between quotation marks in the input string")

    return values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()