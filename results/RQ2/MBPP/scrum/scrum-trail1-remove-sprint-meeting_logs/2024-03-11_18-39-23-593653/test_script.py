def add_string(list_, string):
    if not isinstance(list_, list):
        raise ValueError("list_ must be a list")
    if not isinstance(string, str):
        raise ValueError("string must be a string")

    try:
        new_list = list(map(lambda x: string.format(x), list_))
        return new_list
    except (KeyError, ValueError) as e:
        raise ValueError("Invalid format string: {}".format(e))
    except (TypeError) as e:
        raise ValueError("Non-formatable elements in the list: {}".format(e))
    except Exception as e:
        raise ValueError("An error occurred: {}".format(e))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()