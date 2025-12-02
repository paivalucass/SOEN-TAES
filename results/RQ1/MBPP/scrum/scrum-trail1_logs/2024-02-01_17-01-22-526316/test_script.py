def remove_all_spaces(text):
    if not isinstance(text, str) or not text:
        raise ValueError("Input must be a non-empty string")
    
    # Remove all white spaces using join and split
    modified_text = ''.join(text.split())
    
    return modified_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python  program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()