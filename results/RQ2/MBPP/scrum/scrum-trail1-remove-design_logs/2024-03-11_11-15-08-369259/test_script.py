def occurance_substring(text, pattern):
    import re
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Input arguments must be of type string")

    matches = re.finditer(pattern, text)

    occurrences = []

    for match in matches:
        occurrences.append((match.group(), match.start(), match.end()))

    if not occurrences:
        return None

    return occurrences[0]  # Return the first match
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()