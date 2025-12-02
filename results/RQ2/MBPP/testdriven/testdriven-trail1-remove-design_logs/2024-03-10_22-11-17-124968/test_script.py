def extract_values(text):
    import re
    return re.findall(r'\"(.*?)\"', text)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()