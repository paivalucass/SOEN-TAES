def colon_tuplex(tuplex, index, value):
    try:
        if len(tuplex) > index:
            return tuplex[:index] + (value,) + tuplex[index+1:]
        else:
            return tuplex
    except Exception as e:
        print(f'An error occurred: {e}')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()