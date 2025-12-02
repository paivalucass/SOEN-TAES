def find_literals(text, pattern):
    # Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.

    # Your code here
    import re
    matches = re.search(pattern, text)
    if matches:
        start_index = matches.start()
        end_index = matches.end()
        return (matches.group(), start_index, end_index)
    else:
        return ("Pattern not found", -1, -1)
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

if __name__ == '__main__':
    unittest.main()