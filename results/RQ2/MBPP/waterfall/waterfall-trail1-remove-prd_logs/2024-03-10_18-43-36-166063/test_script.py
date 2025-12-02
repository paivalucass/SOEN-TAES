def find_literals(text, pattern):
    import re
    match = re.search(pattern, text)
    if match:
        start_index = match.start()
        end_index = match.end()
        return (match.group(), start_index, end_index)
    else:
        return None
import re
import unittest

class Test(unittest.TestCase):
    def test_find_literals(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

if __name__ == '__main__':
    unittest.main()