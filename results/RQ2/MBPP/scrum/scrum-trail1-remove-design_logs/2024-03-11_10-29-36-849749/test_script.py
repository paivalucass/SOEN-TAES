def add_string(list_, string):
    if not isinstance(list_, list):
        raise ValueError("Input list must be a list")

    if not isinstance(string, str):
        raise ValueError("Format string must be a string")

    return [string.format(item) for item in list_]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()