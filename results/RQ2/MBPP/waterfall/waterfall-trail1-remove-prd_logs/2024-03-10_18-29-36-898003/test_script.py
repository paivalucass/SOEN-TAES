def tup_string(tup1):
    if isinstance(tup1, tuple):
        str1 = ''.join(str(x) for x in tup1 if isinstance(x, str))
        if len(str1) > 255:
            return str1[:255]
        return str1
    else:
        return "Input is not a tuple"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()