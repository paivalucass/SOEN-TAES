def max_length_list(input_list):
    try:
        if not isinstance(input_list, list):
            raise ValueError("Input is not a list")
        
        if not input_list:
            raise ValueError("Input list is empty")

        max_length = 0
        max_list = []
        for lst in input_list:
            if isinstance(lst, list):
                if len(lst) > max_length:
                    max_length = len(lst)
                    max_list = lst
            else:
                raise ValueError("Input contains non-list elements")

        return (max_length, max_list)

    except ValueError as e:
        raise e

# Test cases
print(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17]))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()