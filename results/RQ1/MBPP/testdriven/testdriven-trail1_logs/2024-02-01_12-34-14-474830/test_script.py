def add_string(list_, string):
    try:
        formatted_list = [string.format(element) for element in list_]
        return formatted_list
    except AttributeError:
        return "Error: 'list_' parameter is not iterable"
    except ValueError:
        return "Error: Invalid format string"
    except Exception as e:
        return "An error occurred: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_string([1,2,3,4],'temp{0}'), ['temp1', 'temp2', 'temp3', 'temp4'])

if __name__ == '__main__':
    unittest.main()