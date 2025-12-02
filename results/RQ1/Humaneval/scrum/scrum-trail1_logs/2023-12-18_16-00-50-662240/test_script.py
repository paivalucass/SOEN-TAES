def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    start = planets.index(planet1)
    end = planets.index(planet2)
    if start < end:
        result = planets[start+1:end]
    else:
        result = planets[end+1:start]
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))
        self.assertEqual(bf('Earth', 'Mercury'), ('Venus'))
        self.assertEqual(bf('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

if __name__ == '__main__':
    unittest.main()