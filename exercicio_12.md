### Análise das funções hash

Considerando M = 10:

#### 1. h₁(k) = k mod 10
Essa função distribui as chaves de acordo com o resto da divisão por 10.
Para chaves bem espalhadas, a distribuição tende a ser boa.
Entretanto, se muitas chaves tiverem o mesmo padrão de resto, ocorrerão colisões.

Exemplo:
- 5, 15, 25, 35 -> todas colidem na posição 5

#### 2. h₂(k) = (k × 7) mod 10
Como 7 é coprimo com 10, essa função apenas permuta os restos possíveis.
Ou seja, para conjuntos amplos e variados, ela preserva uma distribuição semelhante à de h₁.
Ela não elimina colisões estruturais; apenas muda os índices em que elas ocorrem.

Conclusão:
- h₂ tem comportamento muito parecido com h₁ em termos de qualidade de distribuição.

#### 3. h₃(k) = (k²) mod 10
Essa função apresenta maior risco de colisão.
Os quadrados módulo 10 não ocupam todos os buckets com a mesma frequência.
Na prática, certos restos aparecem repetidamente, e alguns buckets podem quase não ser usados.

Exemplos:
- 2² mod 10 = 4
- 8² mod 10 = 4
- 3² mod 10 = 9
- 7² mod 10 = 9

Isso gera mais colisões e pior aproveitamento da tabela.

### Conclusão geral

- **Melhores opções**: h₁ e h₂
- **Maior risco de colisão**: h₃

### Justificativa final
h₁ e h₂ mantêm uma distribuição mais uniforme sobre os 10 buckets quando as chaves são variadas.
Já h₃ concentra chaves em menos posições, aumentando o número de colisões e degradando o desempenho.