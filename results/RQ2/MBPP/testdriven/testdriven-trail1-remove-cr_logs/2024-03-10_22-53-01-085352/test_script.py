def occurrence_substring(text: str, pattern: str) -> List[Tuple[str, int, int]]:
    occurrences = []
    index = 0
    while index < len(text):
        i = text.find(pattern, index)
        if i == -1:
            break
        occurrences.append((pattern, i, i + len(pattern)))
        index = i + len(pattern)
    return occurrences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()