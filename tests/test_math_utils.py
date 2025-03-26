import unittest
import sys
import os

# Añadir el directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import math_utils
import math_utils


class TestUtils(unittest.TestCase):
    def test_es_primo(self):
        self.assertFalse(math_utils.es_primo(4))
        self.assertTrue(math_utils.es_primo(5))
        self.assertEqual(math_utils.es_primo(-5), "No es posible devolver números primos.")
        
        
if __name__=="__main__":
    unittest.main()