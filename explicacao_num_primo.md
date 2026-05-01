# Explicação — Verificação de Número Primo em Python

## O que o código faz

Este módulo implementa uma função que verifica se um número inteiro é primo, seguindo boas práticas de **Clean Code** e otimização algorítmica.

---

## Explicação Linha a Linha

### Importação

```python
import math
```
Importa o módulo `math` da biblioteca padrão do Python para usar a função `isqrt`, que calcula a raiz quadrada inteira de forma eficiente.

---

### Função principal `eh_primo`

```python
def eh_primo(numero: int) -> bool:
```
Define a função com **type hints**: recebe um inteiro (`int`) e retorna um booleano (`bool`). O nome `eh_primo` segue o padrão de nomenclatura legível em português.

---

### Docstring

```python
"""
Verifica se um número inteiro é primo.
...
"""
```
Documenta a função seguindo o padrão **Google Style Docstring**, descrevendo o que faz, os argumentos e o retorno.

---

### Casos base

```python
if numero < 2:
    return False
```
Números menores que 2 (negativos, 0 e 1) **nunca são primos** por definição matemática.

```python
if numero == 2:
    return True
```
O número 2 é o único número primo **par**. Tratado como caso especial para eficiência.

```python
if numero % 2 == 0:
    return False
```
Elimina todos os outros números pares de uma vez, sem precisar verificar divisores pares adiante.

---

### Otimização com raiz quadrada

```python
limite = math.isqrt(numero) + 1
```
**Otimização matemática fundamental:** se um número `n` não possui divisor até `√n`, ele é primo. Isso reduz o número de iterações de `n` para `√n`.

`math.isqrt` retorna a raiz quadrada inteira, evitando imprecisões de ponto flutuante.

```python
for divisor in range(3, limite, 2):
```
Verifica apenas divisores **ímpares** a partir de 3 (pulando de 2 em 2), pois os pares já foram eliminados anteriormente.

```python
    if numero % divisor == 0:
        return False
```
Se encontrar qualquer divisor exato, o número **não é primo**.

```python
return True
```
Se nenhum divisor foi encontrado, o número **é primo**.

---

### Função `main`

```python
def main():
    numeros_para_testar = [1, 2, 3, 4, 17, 20, 97, 100]
    for numero in numeros_para_testar:
        resultado = "primo" if eh_primo(numero) else "não primo"
        print(f"{numero} → {resultado}")
```
Demonstra o uso da função com uma lista de exemplos, usando **f-string** para formatação clara da saída.

---

### Proteção do ponto de entrada

```python
if __name__ == "__main__":
    main()
```
Garante que `main()` só seja executada quando o arquivo for rodado diretamente, e não quando importado como módulo em outro arquivo.

---

## Saída esperada

```
1 → não primo
2 → primo
3 → primo
4 → não primo
17 → primo
20 → não primo
97 → primo
100 → não primo
```

---

## Melhorias aplicadas (Clean Code)

| Antes | Depois |
|---|---|
| Nome genérico `primo(n)` | Nome descritivo `eh_primo(numero)` |
| Sem type hints | `numero: int -> bool` |
| Sem docstring | Docstring completa no padrão Google |
| Loop até `n` (lento) | Loop até `√n` (eficiente) |
| Verificava números pares | Elimina pares antes do loop |
| Sem proteção `__main__` | `if __name__ == "__main__"` |
