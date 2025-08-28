from fizzbuzz.core import fizzbuzz
import unittest 


class TesteMatematica(unittest.TestCase):

    def test_soma_passando(self):  
        resposta = [1,2,'fizz']  
        self.assertEqual(fizzbuzz(3), resposta)    


if __name__ == "__main__":
    unittest.main()

