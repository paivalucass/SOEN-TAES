def extract_values(text):
    import re
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    pattern = r'\"(.*?)\"'
    matches = re.findall(pattern, text)

    if not matches:
        raise ValueError("No values found between quotation marks")

    return matches
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()