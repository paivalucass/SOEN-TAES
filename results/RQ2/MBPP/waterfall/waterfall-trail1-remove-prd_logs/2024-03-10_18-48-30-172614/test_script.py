def occurrence_substring(text, pattern):
    if not text or not pattern:
        return None
    table = [0] * len(pattern)
    i, j = 1, 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
            i += 1
        else:
            if j != 0:
                j = table[j - 1]
            else:
                table[i] = 0
                i += 1
    i, j = 0, 0
    result = []
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                result.append((pattern, i - j, i - 1))
                j = table[j - 1]
        else:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1
    return result if result else None

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()