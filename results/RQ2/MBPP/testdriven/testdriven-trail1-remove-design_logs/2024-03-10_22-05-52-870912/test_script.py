def add_string(list_, string):
    if not isinstance(list_, list) or not isinstance(string, str):
        raise ValueError("list_ must be a list and string must be a string")

    if not list_:
        raise ValueError("list_ cannot be empty")

    return [string.format(item) for item in list_]
import unittest

class Test(unittest.TestCase):
    def test_add_string(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()