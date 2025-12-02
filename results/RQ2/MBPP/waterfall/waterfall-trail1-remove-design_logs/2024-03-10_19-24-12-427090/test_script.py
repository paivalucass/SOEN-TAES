def check_str(input_string):
    import re
    pattern = r'^(?:[aeiouAEIOU]).*'
    if re.match(pattern, input_string):
        return True
    else:
        return False
import unittest
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_str('annie'), True)

if __name__ == '__main__':
    unittest.main()