palavra = input('Digite uma palavra: ')
num_de_vezes = palavra.count('a')
print(f'Na palavra {palavra}, a letra "a" aparece {num_de_vezes} vezes!!!')
if num_de_vezes == 0:
    print(f'Não há letra "a" na palavra {palavra}.')
