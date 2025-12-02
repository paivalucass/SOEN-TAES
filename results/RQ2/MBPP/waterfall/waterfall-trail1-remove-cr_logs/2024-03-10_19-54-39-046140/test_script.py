def tup_string(tup1):
    try:
        return ''.join(map(str, tup1))
    except Exception as e:
        return "Error: Unable to convert tuple to string - " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')), "exercises")

if __name__ == '__main__':
    unittest.main()