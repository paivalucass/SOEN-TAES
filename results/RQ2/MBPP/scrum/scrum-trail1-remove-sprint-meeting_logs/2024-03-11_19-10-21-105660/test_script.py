def occurrence_substring(text, pattern):
    '''Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.'''
    index = text.find(pattern)
    if index != -1:
        return (pattern, index, index + len(pattern))
    else:
        return None

assert occurrence_substring('python programming, python language', 'python') == ('python', 0, 6)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(occurance_substring('python programming, python language', 'python'), ('python', 0, 6))

if __name__ == '__main__':
    unittest.main()