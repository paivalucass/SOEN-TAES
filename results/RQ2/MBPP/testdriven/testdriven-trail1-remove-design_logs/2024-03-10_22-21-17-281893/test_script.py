def occurrence_substring(text, pattern):
    import re
    matches = [(m.group(0), m.start(), m.end()) for m in re.finditer(pattern, text)]
    return matches[0] if matches else None

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()