def extract_values(text):
    import re
    pattern = r'\"(.*?)\"'
    return re.findall(pattern, text)
import unittest

class Test(unittest.TestCase):
    def test_extract_values(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()