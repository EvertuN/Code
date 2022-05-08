# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas nas informações possíveis sobre ele #
key = input('Digite aqui: ')
print('O tipo primitivo desse valor é ', type(key))
print('É número?', key.isnumeric())
print('É letra?', key.isalpha())
print('É alphanumérico?', key.isalnum())
print('É maiúsculo?', key.isupper())
print('É minúsculo?', key.islower())
