def occurrence_substring(text, pattern):
    index = text.find(pattern)
    if index != -1:
        return (pattern, index, index + len(pattern))
    else:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))
        self.assertEqual(occurance_substring('hello world', 'python'), None)

if __name__ == '__main__':
    unittest.main()