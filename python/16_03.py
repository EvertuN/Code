"""
Everton Almeida - UTF-8 - pt br - 16-03-2022
Dinheiro e Variáveis
"""

'''
#Variáveis Numéricas em Python#

#1
v1=1000.15
print(f'O valor da variável v1 é R$: {v1}')
print('\n')

#2
v2=1000.15
print(f'O valor da variável v2 é R$: {v2:,}')
print('\n')

#3
v3=1152024432.15
print(f'O valor da variável v3 é R$:{v3:,}')
print('\n')

#4
v4=1152024432.15
print(f'O valor da variável v3 é R$:{v4:,.5f}')
print('\n')

#5
#Dado o valor em percentual:
valor_percentual=0.06666
print(valor_percentual)
print()
print(f'O valor da variável valor_percentual formatada é:{valor_percentual:,.2%}')

#6 data a variavel
v6=1152024432.15
texto_valor_americano=f'R$:{v6:,.2f}'
print(f'O formato de número americano é:{texto_valor_americano}')
print()

texto_valor_underline=f'R$:{v6:_.2f}'
print(f'O formato de número com uderline é:{texto_valor_underline}')
print()

texto_valor_em_real= texto_valor_underline.replace(".",",").replace("_",".")
print(f'O formato de número com underline é:{texto_valor_em_real}')
print()

#7
v7=1152024432.15
print()
valor=f'R${v7:_.2f}'
print(valor.replace(".",",").replace("_","."))
'''

#Manipulação de Variável do TIPO STRING (STR)#
'''
#1
instituicao='Instituto'
esfera='Federal'
print(instituicao+esfera) # 'Instituto Federal'

#2
instituicao='Instituto Federal de Rondônia'
print('\n')
print('#Recebendo os 17 primeiros caracteres da string')
fatia_1=instituicao[0:17]
print(fatia_1)

#3
instituicao='Instituto Federal de Rondônia'
print('#Recebendo dados a partir do 10° caractere até o caractere 25°')
fatia_2=instituicao[10:25]
print(fatia_2)#'Federal de Rond'

#4
instituicao='Instituto Federal de Rondônia'
print('\n')
print('#Recebendo dados a partir do 10° caracter até o caracter 25°')
fatia_2=instituicao[10:]
print(fatia_2)


instituicao='Instituto Federal de Rondônia'
print('\n')
print('#Recebendo dados do índice 0 até o índice 20, pulando 3 em 3 letras.')
fatia_3= instituicao[0:20:3]
print(fatia_3)

#8 - Concatenando
nome='Marcos'
nome='B' + nome[1:]
print(nome)#Barcos

instituicao='socorram me subi no onibus em marrocos'
print('#Invertendo a ordem dos caracteres que estão dentro da String')
fatia_5=instituicao[::-1]
print(fatia_5)

instituicao='Instituto Federal de Rôndonia'
print('\n')
print('#Recebendo dos dados a partir do índice 5 e finaliza 2 caracteres antes do final')
fatia_4=instituicao[5:-4]
print(fatia_4)

#9 - substituindo letras
nome='Messias'
nome=nome.replace('s','9')
print(nome)

#10 Verificando inicial
nome='Marmelada'
print(nome.startswith('M'))
print(nome.startswith('m'))

#Verificando a letra do final
nome='Messias'
print(nome.endswith('s'))
print(nome.endswith('9'))

#12
nome='Messias'
print(nome.endswith('s')and nome.startswith('M'))
print(nome.endswith('9')and nome.startswith('M'))

# ASC = OBTENDO O CÓDIGO DA TECLA ou LETRA DO CÓDIGO #
print('a'>'X')

print(chr(97))
print(chr(88))

print()

print(ord('a'))
print(ord('X'))

variavel='Campus Ariquemes'
variavel=variavel[::-1]
print(variavel)

#Exercícios trabalhando com tipos numéricos#
"""
5 = inteiro
5.0 = ponto flutuante
4.3 = ponto flutuante
-25 = inteiro
100.00 = ponto flutuante
1.333333 = ponto flutuante
5547 = inteiro
2.88888 = ponto flutuante
9.5 = ponto flutuante
1 = inteiro
"""

#1
vendas_do_dia=1500.00
custo_do_dia=830.00
resultado_do_dia= vendas_do_dia - custo_do_dia
print(f'O resultado do Dia é R$: {resultado_do_dia}')

#2

#a#
salario=2350.00

print()
valor=f'Salario R$:{salario:_.2f}'
print(valor.replace(".",",").replace("_","."))
'''
#b#c#
salario=2350.0
aumento= 0.05
v1= salario * aumento
novo_salario= salario + v1
print()
valor=f'Novo Salário R$:{novo_salario:_.2f}'
print(valor.replace(".",",").replace("_","."))











