def calcular_estatisticas(numeros: list[float]) -> dict:
    """
    Calcula estatísticas básicas de uma lista de números.

    Args:
        numeros (list[float]): Lista de valores numéricos.

    Returns:
        dict: Dicionário contendo total, média, maior e menor valor.
    """
    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    return {
        "total": total,
        "media": media,
        "maior": maior,
        "menor": menor,
    }


def exibir_estatisticas(estatisticas: dict) -> None:
    """
    Exibe as estatísticas calculadas de forma formatada.

    Args:
        estatisticas (dict): Dicionário retornado por calcular_estatisticas.
    """
    print(f"Total:  {estatisticas['total']}")
    print(f"Média:  {estatisticas['media']:.2f}")
    print(f"Maior:  {estatisticas['maior']}")
    print(f"Menor:  {estatisticas['menor']}")


def main():
    """Executa o cálculo e exibição de estatísticas para uma lista de exemplo."""
    valores = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    estatisticas = calcular_estatisticas(valores)
    exibir_estatisticas(estatisticas)


if __name__ == "__main__":
    main()
