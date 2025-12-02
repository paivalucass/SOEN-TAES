def by_length(arr):
    num_to_word = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    filtered_arr = [num for num in arr if 1 <= num <= 9]
    filtered_arr.sort()
    filtered_arr.reverse()

    result = [num_to_word[num] for num in filtered_arr]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([2, 1, 1, 4, 5, 8, 2, 3]), ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])

if __name__ == '__main__':
    unittest.main()