import unittest
from main import suma

class TestSuma(unittest.TestCase):
    def test_suma_simple(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativa(self):
        self.assertEqual(suma(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

