def remove_all_spaces(text):
    if text.strip():  
        return text.replace(" ", "")
    else:
        return "Input string is empty or contains only whitespaces"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()