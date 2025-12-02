def occurrence_substring(text, pattern):
    occurrences = []
    start = 0
    while start < len(text):
        start = text.find(pattern, start)
        if start == -1:
            break
        end = start + len(pattern)
        occurrences.append((text[start:end], start, end))
        start = end
    return occurrences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 5))

if __name__ == '__main__':
    unittest.main()