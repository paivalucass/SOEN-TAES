def remove_nested(test_tup):
    try:
        if not isinstance(test_tup, tuple):
            raise TypeError("Input should be a tuple")
        result = tuple([item for item in test_tup if not isinstance(item, tuple)])
        return result
    except TypeError as e:
        print(f"An error occurred: {e}")

# Testing the function
assert remove_nested(()) == ()
assert remove_nested((1, 2, 3)) == (1, 2, 3)
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
assert remove_nested(((1, 2), 3, (4, 5), (6, 7, 8))) == (3,)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_nested((1, 5, 7, (4, 6), 10)), (1, 5, 7, 10))

if __name__ == '__main__':
    unittest.main()