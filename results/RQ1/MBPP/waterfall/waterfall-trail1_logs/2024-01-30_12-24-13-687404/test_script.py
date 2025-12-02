def word_len(s: str) -> bool:
    if not s:
        return False
    if not s.isalpha():
        return True
    return len(s) % 2 != 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()