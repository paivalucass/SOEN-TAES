def start_withp(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of words")
    p_words = [word for word in words if word.lower().startswith('p') and len(word.split()) == 1]
    return tuple(p_words[:2])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()