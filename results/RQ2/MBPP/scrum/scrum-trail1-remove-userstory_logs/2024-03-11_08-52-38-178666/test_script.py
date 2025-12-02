def merge_dictionaries_three(dict1, dict2, dict3):
    result = dict1.copy()
    result.update(dict2)
    result.update(dict3)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }), {'R': 'Red', 'B': 'Black', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'})

if __name__ == '__main__':
    unittest.main()