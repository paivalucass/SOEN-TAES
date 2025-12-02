def remove_all_spaces(text):
    if text is None or not isinstance(text, str):
        raise ValueError("Input must be a valid string")

    import re
    result = re.sub(r'\s+', '', text)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()