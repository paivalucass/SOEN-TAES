from typing import Union

def strlen(string: Union[str, None]) -> Union[int, str]:
    if isinstance(string, str):
        return len(string)
    else:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(strlen(''), 0)
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()