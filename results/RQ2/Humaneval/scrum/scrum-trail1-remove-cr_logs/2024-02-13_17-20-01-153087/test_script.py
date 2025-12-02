def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 in planets and planet2 in planets:
        start = planets.index(planet1)
        end = planets.index(planet2)
        if start < end:
            return tuple(sorted(planets[start+1:end], key=lambda x: planets.index(x)))
        else:
            return tuple(sorted(planets[end+1:start], key=lambda x: planets.index(x), reverse=True))
    else:
        return ()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

if __name__ == '__main__':
    unittest.main()