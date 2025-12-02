def occurance_substring(text, pattern):
    import re
    match = re.search(pattern, text)
    if match:
        return (pattern, match.start(), match.end())
    else:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))
        self.assertEqual(occurance_substring('hello world', 'python'), None)

if __name__ == '__main__':
    unittest.main()