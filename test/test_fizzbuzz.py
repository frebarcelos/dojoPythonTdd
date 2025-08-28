from fizzbuzz.core import fizzbuzz

def test_deve_retornar_fizz_para_3():
    """
    Testa se a função retorna 'Fizz' para 3.
    """
    assert fizzbuzz(3) == "Fizz"
    