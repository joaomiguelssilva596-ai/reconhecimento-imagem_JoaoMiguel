import math


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é aquele maior que 1 que não possui
    divisores além de 1 e ele mesmo.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    limite = math.isqrt(numero) + 1
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False

    return True


def main():
    """Executa exemplos de verificação de números primos."""
    numeros_para_testar = [1, 2, 3, 4, 17, 20, 97, 100]

    for numero in numeros_para_testar:
        resultado = "primo" if eh_primo(numero) else "não primo"
        print(f"{numero} → {resultado}")


if __name__ == "__main__":
    main()
