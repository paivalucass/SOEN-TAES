def find_adverb_position(text):
    import re
    adverb_positions = [(m.start(), m.end(), m.group()) for m in re.finditer(r'\b\w+ly\b', text)]
    return adverb_positions[0]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position("clearly!! we can see the sky"), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()