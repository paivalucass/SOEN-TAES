def remove_dirty_chars(input_string: str, dirty_chars: str) -> str:
    if not input_string or not dirty_chars:
        return ""
    
    dirty_set = set(dirty_chars)
    result = [char for char in input_string if char not in dirty_set]
    return ''.join(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()