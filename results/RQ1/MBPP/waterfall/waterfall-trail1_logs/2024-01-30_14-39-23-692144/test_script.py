def extract_values(text):
    import re
    values = re.findall(r'\"(.*?)\"', text)
    return values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()