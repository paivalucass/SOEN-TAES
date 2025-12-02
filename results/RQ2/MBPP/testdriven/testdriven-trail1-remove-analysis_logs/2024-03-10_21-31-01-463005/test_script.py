def remove_all_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text.replace(' ', '')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python  program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()