def word_len(s: str) -> int:
    if len(s) % 2 == 0:
        return 0
    else:
        return 1
import unittest

class Test(unittest.TestCase):
    def test_word_len(self):
        self.assertEqual(word_len("Hadoop"), False)

if __name__ == '__main__':
    unittest.main()