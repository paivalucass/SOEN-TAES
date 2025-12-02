def remove_all_spaces(text):
    import re
    if text is None or text == "":
        return ""
    else:
        return re.sub(r'\s+', '', text)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_all_spaces('python program'), 'pythonprogram')

if __name__ == '__main__':
    unittest.main()