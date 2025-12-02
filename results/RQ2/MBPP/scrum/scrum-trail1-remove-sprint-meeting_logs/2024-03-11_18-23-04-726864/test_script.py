def tup_string(tup1: tuple) -> str:
    result = ""
    if isinstance(tup1, tuple):
        for item in tup1:
            if isinstance(item, str):
                result += item
            else:
                raise ValueError("Input tuple contains non-string elements")
    else:
        raise ValueError("Input is not a tuple")
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()