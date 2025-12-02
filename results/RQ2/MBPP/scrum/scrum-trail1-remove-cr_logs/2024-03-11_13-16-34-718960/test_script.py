def concatenate_tuple(test_tup, delimiter='-'):
    try:
        result = ''
        for i in range(len(test_tup)):
            result += str(test_tup[i])
            if i < len(test_tup) - 1:
                result += delimiter
        return result
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test_concatenate_tuple(self):
        self.assertEqual(concatenate_tuple(("ID", "is", 4, "UTS")), 'ID-is-4-UTS')

if __name__ == '__main__':
    unittest.main()