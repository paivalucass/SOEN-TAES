def add_string(list_, string):
    if not list_:
        return []

    if not isinstance(string, str):
        raise ValueError("Invalid format string")

    result = []
    for element in list_:
        result.append(string.format(element))

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4], 'temp{}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()