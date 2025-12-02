def start_withp(words):
    result = []
    for word in words:
        split_words = word.split()
        for split_word in split_words:
            if split_word.startswith('p') or split_word.startswith('P'):
                result.append(split_word)
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()