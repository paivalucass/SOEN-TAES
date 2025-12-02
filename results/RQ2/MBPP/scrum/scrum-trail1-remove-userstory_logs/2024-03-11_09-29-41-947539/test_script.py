def remove_all_spaces(text):
    modified_text = "".join(text.split())
    return modified_text

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python  program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()