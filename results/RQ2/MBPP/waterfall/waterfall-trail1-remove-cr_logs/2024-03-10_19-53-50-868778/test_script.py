def string_to_list(string):
    try:
        if len(string) == 0:
            return []
        else:
            result = string.split()
            return result
    except Exception as e:
        return "Error: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()