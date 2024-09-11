def bem_vindo():
    print('Bem vindo a sequencia de Fibonacci')
    print('A sequência começa com: 0, 1... tente adivinhar o próximo número!')

def obter_quantidade():
    return int(input('Até quantos números quer tentar adivinhar? '))

def verificar_fibonacci(t1, t2, quant):
    fibb = [0, 1]
    for _ in range(quant):
        t3 = int(input('Digite o próximo número da sequência: '))
        if t3 == t1 + t2:
            t1, t2 = t2, t3
            fibb.append(t3)
            print(f'O número {t3} pertence a sequência de fibonacci')
        else:
            print(f'{t3} não pertence à sequência.')
        print(f'A sequência está {fibb}')
    return fibb

def main():
    bem_vindo()
    quant = obter_quantidade()
    fibb = verificar_fibonacci(0, 1, quant)
    print(f'Muito bem!!! você achou os {quant + 2} primeiros números da sequência de {fibb}')

if __name__ == "__main__":
    main()