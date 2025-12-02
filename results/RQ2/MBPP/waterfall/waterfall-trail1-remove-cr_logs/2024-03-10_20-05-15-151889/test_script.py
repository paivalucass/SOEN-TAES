def find_adverb_position(text):
    import re
    match = re.search(r'\b\w+ly\b', text)
    if match:
        return (match.start(), match.end(), match.group())
    else:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position("clearly!! we can see the sky"), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()