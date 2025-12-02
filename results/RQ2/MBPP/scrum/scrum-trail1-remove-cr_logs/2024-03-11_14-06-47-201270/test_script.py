def remove_all_spaces(text):
    return ''.join(text.split())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python  program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()