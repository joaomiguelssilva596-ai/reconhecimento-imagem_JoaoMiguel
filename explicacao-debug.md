# Explicação — Debug com IA

## Código original com erros

O código fornecido simulava um sistema de cupom fiscal simples em Python. Ao analisar com a IA, foram identificados **4 erros**, sendo 2 de sintaxe e 2 de lógica/tipo.

---

## Erros Encontrados e Corrigidos

---

### Erro 1 — String ausente no `input()` (Sintaxe)

**Linha original:**
```python
item1 = float(input(Preço do item 1? ))
```

**Problema:**
O argumento do `input()` não estava entre aspas. Em Python, texto literal precisa ser uma string. Sem as aspas, o interpretador tenta avaliar `Preço do item 1?` como código Python, gerando `SyntaxError`.

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### Erro 2 — `input()` sem conversão de tipo (Lógica/Tipo)

**Linha original:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

**Problema:**
`input()` sempre retorna uma **string** em Python. O código depois tenta fazer `subtotal * (desconto_cupom / 100)`, que é uma divisão em string — isso gera `TypeError`. Além disso, a comparação `if desconto_cupom > 0` também falharia, pois não se compara string com número.

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

---

### Erro 3 — f-string ausente (Sintaxe)

**Linha original:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Problema:**
Faltou o prefixo `f` antes das aspas. Sem o `f`, o Python trata o texto como uma string comum e imprime literalmente `{total_item2:.2f}` em vez do valor da variável.

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

### Erro 4 — Indentação incorreta no bloco `if` (Sintaxe)

**Linha original:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Problema:**
Em Python, o corpo de um bloco `if` deve estar **indentado** (recuado com espaços ou tab). Sem a indentação, o interpretador gera `IndentationError`.

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## Resumo dos Erros

| # | Tipo | Linha | Descrição |
|---|---|---|---|
| 1 | `SyntaxError` | `item1 = float(input(...))` | String sem aspas dentro do `input()` |
| 2 | `TypeError` | `desconto_cupom = (input(...))` | Valor de `input()` não convertido para `float` |
| 3 | `SyntaxError` | `print(" Item 2: ...")` | f-string sem o prefixo `f` |
| 4 | `IndentationError` | `print(f" Desconto...")` | Corpo do `if` sem indentação |

---

## Lição aprendida

A IA foi capaz de identificar erros de **sintaxe** (que impedem o programa de rodar) e erros de **lógica de tipos** (que causam falhas em tempo de execução). Sempre fornecer o código completo para a IA facilita a análise do contexto e resulta em diagnósticos mais precisos.
