#Ordem de Precêdencia
"""
1 - ()
2 - **
3 - * / // %
4 - + -
"""
"""
nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer {nome:20}!')
"""
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma de {s}, o produto é {m}, e a divisão é {d:.3}', end='>>>')
print(f'Divisão inteira  {di} e potência {e}')