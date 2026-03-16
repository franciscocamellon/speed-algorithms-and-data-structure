## Função analisada

`knapsack(target, weights, index)`

## Ideia

Para cada posição `index`, a função cria dois ramos:

- incluir `weights[index]`
- não incluir `weights[index]`

## Chamadas redundantes

O mesmo subproblema pode ser recalculado várias vezes.

O estado do problema é definido por:

- `target`
- `index`

Logo, chamadas com o mesmo par `(target, index)` são redundantes.

## Crescimento do número de chamadas

No pior caso, para cada item há duas escolhas.  
Isso gera aproximadamente uma árvore binária de altura `n`.

## Complexidade

- **Tempo:** `O(2^n)` no pior caso
- **Espaço de pilha:** `O(n)`

## Conclusão

A versão recursiva pura é correta e didática, mas não é eficiente para entradas maiores.  
Ela é um bom exemplo do que a Aula 11 chama de reexame de subproblemas já resolvidos, motivando programação dinâmica.