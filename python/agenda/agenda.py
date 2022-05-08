"""
Everton Almeida - UTF-8 - pt-br - 27-04-2022
Manipulando agenda de contatos
"""
nome: []
email: []
tfone: []
vlr_hora: []
sair = ''
saida_final = ''

print('\n')
print('Agenda de contatos')
print('\n')

while saida_final.upper() != "N":
    print('1-Insere')
    while sair.upper() != "N":
        nome = input('Nome completo: ')
        email = input('Nome completo: ')
        tfone = input('Nome completo: ')
        vlr_hora = input('Nome completo: ')

        nomes.append(nome)
        emails.append(email)
        tfones.append(tfone)
        vlr_hora.append(vlr_hora)

        print('\n')
        sair = input('Digitar outro contato? (s/n): ')
        if sair sair.upper() != "N":
            saida_final.upper() = "S"

    print('\n')
