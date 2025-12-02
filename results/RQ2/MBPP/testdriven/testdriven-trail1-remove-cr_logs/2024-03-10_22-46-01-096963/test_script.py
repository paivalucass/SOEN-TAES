def list_tuple(input_list):
    try:
        if not isinstance(input_list, list):
            raise TypeError("Input is not a list")

        if len(input_list) == 0:
            raise ValueError("Input list is empty")

        for element in input_list:
            if not isinstance(element, (int, float, str)):
                raise ValueError("Elements of the list should be of type int, float, or str")

        return tuple(input_list)

    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()