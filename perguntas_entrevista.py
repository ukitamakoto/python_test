# Função que inverte uma string
def reverse_string(word):
    return ''.join(reversed(word))

# Teste. Verificação da função reverse_string
def test_reverse_string():
    input_str = "TripleTen"

    # Realize a operação inversa
    reversed_str = reverse_string(input_str)

    # Verifique se a string invertida corresponde ao resultado esperado
    assert reversed_str == "neTelpirT"

    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)


# Função para verificar palíndromo
def is_palindrome(word):
    # Inverta a string usando reversed() e join().
    reversed_str = ''.join(reversed(word))
    return word == reversed_str


# Teste. Verificação da função is_palindrome
def test_is_palindrome():
    # Defina a string de entrada
    input_str = "osso"

    # Execute a verificação do palíndromo
    result = is_palindrome(input_str)

    # Verifique se o resultado é True (verdadeiro) para um palíndromo
    assert result == True

    print("Teste aprovado! '" + input_str + "' é um palíndromo.")

