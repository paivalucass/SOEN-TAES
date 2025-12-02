def add_string(list_, string):
    if list_ is None or not isinstance(list_, list):
        return "Error: Invalid input"
    if not isinstance(string, str) or not string.endswith('{}'):
        return "Error: Invalid format string"
    result = [string.format(element) for element in list_]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4],'temp{}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()