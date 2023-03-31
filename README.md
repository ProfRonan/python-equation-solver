# Calculadora de Raízes

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

Faça um programa que receba um número indicando qual o grau da equação, se esse número for menor do que `1` ou maior do que `2`, o programa deve imprimir `Grau inválido`.

1. Se o grau for `1`, o programa deve imprimir `A equação é do primeiro grau`.
   Em seguida ele deve pedir para o usuário digitar o valor de `a`.
   Caso o usuário digite `0` para `a`, o programa deve imprimir `Valor de a inválido` e terminar o programa.
   Se o usuário digitar um valor diferente de `0` para `a`, o programa deve pedir para o usuário digitar o valor de `b` e imprimir o valor da raiz da da equação `ax + b = 0` com exatamente duas casas decimais, independentemente se o número for inteiro ou não.
2. Se o grau for `2`, o programa deve imprimir `A equação é do segundo grau`.
   Em seguida ele deve pedir para o usuário digitar o valor de `a`.
   Caso o usuário digite `0` para `a`, o programa deve imprimir `Valor de a inválido` e terminar.
   1. Se o usuário digitar um valor diferente de `0` para `a` o programa deve pedir os valores `b` e `c` correspondente à equação `ax² + bx + c = 0`.
   2. Caso o valor de `b² - 4ac` seja menor do que `0`, o programa deve imprimir `A equação não possui raízes reais` e terminar.
   3. Caso o valor de `b² - 4ac` seja igual a `0`, o programa deve imprimir `A equação possui uma raiz real`.
      Em seguida ele deve imprimir o valor da raiz com exatamente duas casas decimais, independentemente se o número for inteiro ou não.
   4. Caso o valor de `b² - 4ac` seja maior do que `0`, o programa deve imprimir `A equação possui duas raízes reais`.
      Em seguida ele deve imprimir o valor das raízes com exatamente duas casas decimais, independentemente se o número for inteiro ou não e terminar.

## ❗ IMPORTANTE ❗

Veja as instruções sobre como proceder com o exercício no link [Instruções Gerais Para os Exercícios](https://github.com/ProfRonan/python-exercise-instructions).
