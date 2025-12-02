def occurance_substring(text, pattern):
    if not text or not pattern:
        return None

    try:
        start_index = text.index(pattern)
        end_index = start_index + len(pattern)
        return (pattern, start_index, end_index)
    except ValueError:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()