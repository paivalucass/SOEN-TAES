def merge_dictionaries_three(dict1, dict2, dict3):
    combined_dict = {**dict1, **dict2, **dict3}
    return combined_dict
import unittest

class Test(unittest.TestCase):
    def test_merge_dictionaries_three(self):
        self.assertEqual(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }), {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'})

if __name__ == '__main__':
    unittest.main()