def all_characters_same(input_string):
    if len(input_string) < 2:
        return False
    first_char = input_string[0]
    for char in input_string[1:]:
        if char != first_char:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_all_characters_same(self):
        self.assertEqual(all_Characters_Same('python'), False)

if __name__ == '__main__':
    unittest.main()