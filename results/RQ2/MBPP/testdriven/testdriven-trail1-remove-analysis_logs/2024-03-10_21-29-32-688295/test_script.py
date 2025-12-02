def occurrence_substring(text, pattern):
    if not text or not pattern:
        return None
    positions = []
    start = 0
    while True:
        start = text.find(pattern, start)
        if start == -1:
            break
        end = start + len(pattern)
        positions.append((text[start:end], start, end-1))
        start += len(pattern)
    if len(positions) == 0:
        return None
    else:
        return positions
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()