# LeetCode em Python

Este repositório contém minhas soluções para problemas do LeetCode usando Python.
Ele reflete meus momentos me divertindo com a linguagem enquanto pratico estruturas de dados, padrões e raciocínio lógico.
Também serve como registro histórico da minha evolução, dos desafios mais simples até os mais complexos.

## Estrutura

As soluções estão separadas por tema:

```text
array_string/
prefix_sum/
sliding_window/
two_pointers/
```

## Catálogo resumido

### `array_string`

- `merge_strings_alternately.py`  
  LeetCode 1768 - Merge Strings Alternately.  
  O que faz: intercala os caracteres de duas strings e adiciona o restante da maior no fim.  
  Como resolvi: loop até o tamanho máximo, adicionando letra por letra de cada string quando existir índice válido.

- `greatest_common_divisor_of_strings.py`  
  LeetCode 1071 - Greatest Common Divisor of Strings.  
  O que faz: encontra a maior string que divide duas strings por repetição.  
  Como resolvi: valido padrão com concatenação (`str1 + str2 == str2 + str1`) e uso `gcd` dos tamanhos para cortar o prefixo correto.

- `kids_with_the_greatest_number_of_candies.py`  
  LeetCode 1431 - Kids With the Greatest Number of Candies.  
  O que faz: retorna quais crianças podem chegar ao maior número de doces com os extras.  
  Como resolvi: pego o máximo atual da lista e comparo cada valor somado aos doces extras.

### `two_pointers`

- `is_subsequence.py`  
  LeetCode 392 - Is Subsequence.  
  O que faz: verifica se uma string `s` é subsequência de `t`.  
  Como resolvi: avanço um ponteiro em `s` enquanto percorro `t` até casar todos os caracteres.

- `move_zeroes.py`  
  LeetCode 283 - Move Zeroes.  
  O que faz: move todos os zeros para o final mantendo a ordem dos não zeros.  
  Como resolvi: uso ponteiro de posição para compactar não zeros no início e preencho o restante com zero.

### `sliding_window`

- `maximum_average_subarray.py`  
  LeetCode 643 - Maximum Average Subarray I.  
  O que faz: calcula a maior média de subarray com tamanho fixo `k`.  
  Como resolvi: mantenho soma da janela atual, deslizo removendo o que sai e somando o que entra, e guardo a maior soma.

### `prefix_sum`

- `find_pivot_index.py`  
  LeetCode 724 - Find Pivot Index.  
  O que faz: encontra o índice onde soma da esquerda e da direita são iguais.  
  Como resolvi: calculo soma total, acumulo soma da esquerda e comparo com a soma da direita em cada posição.

- `find_the_highest_altitude.py`  
  LeetCode 1732 - Find the Highest Altitude.  
  O que faz: retorna a maior altitude atingida a partir de variações de ganho/perda.  
  Como resolvi: acumulo altitude atual e atualizo o máximo encontrado durante a travessia.

## Como executar

No diretório raiz:

```bash
python caminho/do/arquivo.py
```

Exemplo:

```bash
python two_pointers/is_subsequence.py
```
