def my_dict(dict1: dict) -> bool:
    if len(dict1) == 0:
        return True
    else:
        return False

# Test cases
assert my_dict({}) == True
assert my_dict({'key': 'value'}) == False
assert my_dict({'a': 1, 'b': 2, 'c': 3}) == False
assert my_dict({'a': {'x': 1, 'y': 2}, 'b': {'z': 3}}) == False
assert my_dict({'a': {}, 'b': {}}) == False
assert my_dict({10}) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({10}), False)

if __name__ == '__main__':
    unittest.main()