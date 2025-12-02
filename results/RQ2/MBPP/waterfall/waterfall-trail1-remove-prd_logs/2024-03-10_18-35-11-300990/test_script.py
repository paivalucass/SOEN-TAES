def start_withp(words):
    p_words = [word for word in words if word.lower().startswith('p')]
    
    if len(p_words) < 2:
        return None
    
    return tuple(p_words[:2])
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()