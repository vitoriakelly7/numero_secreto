import random

numero_secreto = random.randint(1, 10)
acertou = False
tentativas = 0
max_tentativas = 5

print('   VAMOS JOGAR   ')
print(f'Você tem {max_tentativas} chances para acertar.')
print()

while not acertou and tentativas < max_tentativas:
    chute = int(input('Digite um númro entre 1 e 10: '))
    tentativas += 1

    if chute == numero_secreto:
        print(f'ACERTOU! Você precisou de {tentativas} tentativas.')
        acertou = True #vai parar o loop
    else:
        if tentativas < max_tentativas:
            print(f'ERROU! Tente novamente. Restam {max_tentativas - tentativas} tentativa(s)')
        else:
            print(f'FIM DE JOGO! O número secreto era {numero_secreto}.')
