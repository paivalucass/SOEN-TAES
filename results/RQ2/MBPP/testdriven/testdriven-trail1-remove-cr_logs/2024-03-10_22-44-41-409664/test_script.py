def extract_values(text):
    import re
    return [value for pair in re.findall(r'(?:"([^"]*)"|\'([^\']*)\')', text) for value in pair if value]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()