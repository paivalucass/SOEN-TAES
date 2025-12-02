import re
def occurrence_substring(text, pattern):
    matches = re.finditer(pattern, text)
    result = [(match.group(), match.start(), match.end() - 1) for match in matches]
    return result if result else None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()