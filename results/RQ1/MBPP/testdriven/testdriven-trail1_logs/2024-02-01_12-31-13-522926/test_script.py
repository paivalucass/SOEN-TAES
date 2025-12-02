def start_with_p(words):
    if not words:
        raise ValueError("Input list of words is empty")

    if not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of words")

    p_words = [word for word in words if word.lower().startswith('p')]

    if len(p_words) < 2:
        raise ValueError("There are less than two words starting with 'p'")

    return tuple(p_words[:2])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()