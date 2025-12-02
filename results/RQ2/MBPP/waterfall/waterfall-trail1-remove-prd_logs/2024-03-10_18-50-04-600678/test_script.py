def remove_all_spaces(text):
    if text is None or len(text) == 0:
        return "Error: Invalid input"

    return ''.join([char for char in text if char != ' '])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()