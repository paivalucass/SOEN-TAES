def strlen(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError("Input must be a string")

    return len(string)

# Test Cases
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('abcdefghijklmnopqrstuvwxyz') == 26
    assert strlen('!@#$%^&*()') == 10
    assert strlen('123456789') == 9

if __name__ == "__main__":
    test_strlen()
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)
    
    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()