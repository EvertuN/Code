"""
Everton Almeida - UTF-8 - pt-br - 30-03-2022
ESTRUTURA DE CONTROLE - TOMADA DE DECISÃO
"""

'''
try: #tente executar as  linhas 7, 8, 9 
    nome=input('Digite seu nome:')
    disciplina=input('Digite o nome da disciplina:')
    nota=float(input('Digite sua nota:'))
    if len(nome)==0:
        print('Digite um nome válido')
    if len(nome)==0:
        print('Digite uma disciplina válida')
        
except ValueError:
    print('Digite uma nota válida')
finally:
    print('Bloco Finalizado')
if nota >=60:
    mensagem='Você passou. Parabéns!!!'
else:
    mensagem='Você está de exame'
print('Acadêmico(a)')
print('Disciplina:', disciplina)
print('Nota do semestre:', nota)
print('Situação na disciplina:', mensagem)

#entrada de dados
nome=input('Digite o nome do cliente')
ano_nasc=int(input('Digite o ano de nascimento do cliente com quatro dígitos:')
idade=2022-ano_nasc

#proccessamento
if idade<18:
    mensagem='Entrada acompanhado dos pais ou responsáveis.'
elif idade<=21:
    mensagem='Entra pagando ingresso normal.'
else:
    mensagem='Entrada pagando um acréscimo pelo ingresso'

#saída de dados
print('\n')
print('Cliente:', nome)
print('Situação:', mensagem)

#Atividade Avaliativa 30-03-2022#

#a
try: #'n' para nota
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    n3=float(input('Nota 3: '))
    n4=float(input('Nota 4: '))
    print()
except (ValueError, NameError):
    print('Digite apenas números')
    media=(n1+n2+n3+n4)/4
    print(f'Sua média é: {media:.2f}')
    if media>=60:
        mensagem='Aprovado'
    elif media>=40:
        mensagem='Exame'
    elif media>=30:
        mensagem='Só o conselho para ajudar'
    elif media<30:
        mensagem='Retido na disciplina'
finally:
    ''
print(mensagem)

#b
try:
    t=float(input('Tempo gasto para chegar? '))
    vm=float(input('Qual a velocidade média? '))

except ValueError:
    print('Digite apenas números')
    
print(f'Distância percorrida: {vm*t:.2f}Km')
print(f'Quantidade de litros gasto: {vm*t/12.3:.2f}L')
print(f'Valor gasto com combustível: R$ {7.59*(vm*t)/12.3:.2f}')

#c
print("[ATIVIDADE  I]")
x=25
y=42
if x>y:
    print("Acertei")
elif x==y:
    print("Ok")
else:
    print("Errei")

#d
print("\n[ATIVIDADE II]")
if not((15>14)and("a"=="b"))or(12*4)<48 and 1==1:
    print("Passei")
else:
    print("Não passei")
'''
#e















