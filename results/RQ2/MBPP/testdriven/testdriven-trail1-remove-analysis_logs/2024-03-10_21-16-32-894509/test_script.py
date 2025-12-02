def start_withp(words):
    if not isinstance(words, list) or len(words) == 0:
        return ()
    
    p_words = [subword for word in words for subword in word.split() if subword.startswith('p')]
    
    return tuple(p_words[:2])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()