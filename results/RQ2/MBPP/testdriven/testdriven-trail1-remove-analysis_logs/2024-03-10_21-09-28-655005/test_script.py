def len_log(word_list):
    if not word_list:
        return 0
    max_length = 0
    for word in word_list:
        if not isinstance(word, str):
            raise ValueError("Input list should only contain strings")
        max_length = max(max_length, len(word))
    return max_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python", "PHP", "bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()