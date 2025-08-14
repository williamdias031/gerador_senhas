import random
import string

def gerar_senha(tamanho=12):
    """
    Gera uma senha aleatória com letras, números e símbolos.
    :param tamanho: tamanho da senha (padrão: 12)
    :return: string com a senha gerada
    """

    # Letras maiúsculas e minúsculas
    letras = string.ascii_letters  # abc...XYZ
    # Dígitos
    numeros = string.digits        # 0123456789
    # Símbolos
    simbolos = string.punctuation  # !@#$%...

    # Junta tudo em um único conjunto de caracteres
    todos_caracteres = letras + numeros + simbolos

    # Gera senha aleatória usando random.choice()
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha


if __name__ == "__main__":
    print("=== GERADOR DE SENHAS SEGURAS ===")
    
    # Pede o tamanho da senha
    try:
        tamanho_senha = int(input("Digite o tamanho da senha (padrão 12): ") or 12)
    except ValueError:
        print("Valor inválido! Usando tamanho padrão de 12.")
        tamanho_senha = 12

    # Gera e exibe a senha
    senha_final = gerar_senha(tamanho_senha)
    print(f"\nSua senha gerada: {senha_final}")
