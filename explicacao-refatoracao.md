# Explicação — Refatoração de Código Python

## Código Original (com problemas)

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

---

## Problemas Identificados

### 1. Nomes de função e variáveis sem significado
- `c` → não indica o que a função faz
- `l`, `t`, `m`, `mx`, `mn`, `x`, `a`, `b`, `d` → letras isoladas sem contexto

### 2. Uso desnecessário de `range(len(lista))`
- O Python permite iterar diretamente sobre listas
- `for i in range(len(l)): ... l[i]` é mais verboso e menos idiomático que `for item in lista`

### 3. Retorno de múltiplos valores sem estrutura
- `return t, m, mx, mn` retorna uma tupla solta, difícil de usar e de documentar

### 4. Ausência de docstring e comentários
- Impossível entender o propósito da função sem ler cada linha

### 5. Lógica manual para operações já disponíveis no Python
- Calcular soma com loop manual em vez de `sum()`
- Calcular maior/menor com loop manual em vez de `max()` / `min()`

---

## Código Refatorado

```python
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
    """Exibe as estatísticas calculadas de forma formatada."""
    print(f"Total:  {estatisticas['total']}")
    print(f"Média:  {estatisticas['media']:.2f}")
    print(f"Maior:  {estatisticas['maior']}")
    print(f"Menor:  {estatisticas['menor']}")


def main():
    valores = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    estatisticas = calcular_estatisticas(valores)
    exibir_estatisticas(estatisticas)


if __name__ == "__main__":
    main()
```

---

## Comparativo das Melhorias

| Problema original | Solução aplicada |
|---|---|
| Função chamada `c` | Renomeada para `calcular_estatisticas` |
| Variáveis `l`, `t`, `m`, `mx`, `mn` | Renomeadas para `numeros`, `total`, `media`, `maior`, `menor` |
| `for i in range(len(l))` | Substituído por `sum()`, `max()`, `min()` |
| Retorno como tupla solta | Retorno como dicionário nomeado |
| Sem docstring | Docstrings completas em todas as funções |
| Lógica de exibição misturada ao cálculo | Separada em função `exibir_estatisticas` |
| Sem proteção `__main__` | Adicionado `if __name__ == "__main__"` |

---

## Explicação Linha a Linha do Código Refatorado

```python
def calcular_estatisticas(numeros: list[float]) -> dict:
```
Define a função com **type hints** claros: recebe uma lista de floats e retorna um dicionário.

```python
total = sum(numeros)
```
Usa a função nativa `sum()` — mais legível e eficiente que um loop manual.

```python
media = total / len(numeros)
```
Calcula a média dividindo o total pelo número de elementos.

```python
maior = max(numeros)
menor = min(numeros)
```
Usa as funções nativas `max()` e `min()` — eliminam os dois loops do código original.

```python
return {"total": total, "media": media, "maior": maior, "menor": menor}
```
Retorna um dicionário com chaves nomeadas, tornando o resultado autoexplicativo.

```python
def exibir_estatisticas(estatisticas: dict) -> None:
```
Função separada com responsabilidade única: só exibe os dados.

```python
if __name__ == "__main__":
    main()
```
Garante que o código de execução só rode quando o arquivo for chamado diretamente.
