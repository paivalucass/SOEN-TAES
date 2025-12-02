def word_len(s: str) -> bool:
    try:
        if not isinstance(s, str) or s == "":
            raise ValueError("Input must be a non-empty string")
        
        return len(s) % 2 != 0
    except ValueError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()