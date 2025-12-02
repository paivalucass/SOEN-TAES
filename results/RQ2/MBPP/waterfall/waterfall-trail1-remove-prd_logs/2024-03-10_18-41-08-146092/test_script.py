def extract_values(text):
    values = text.replace('\"', '').split(',')
    return [value.strip() for value in values if value.strip()]
import unittest

class Test(unittest.TestCase):

    def test_extract_values(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()