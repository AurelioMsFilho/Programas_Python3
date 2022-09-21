'''Escreva um program que leia um número inteiro qualquer e faça para o usário escolher qual será a base de conversão:
-1 binário
-2 octal
 -3 hexadecimal '''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
-1 binário
-2 octal
-3 hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O numero digitado foi {num} e em Binário ele é {bin(num)}')
elif opcao == 2:
    print(f'O numero digitado foi {num} e em Octal ele é {oct(num)}')
elif opcao ==3:
    print(f'O numero digitado foi {num} e em Octal ele é {hex(num)}')
else:
    print('digite um numero ou numero inválido. Tente novamente')

