# Sorteio-de-funcion-rios
sorteio simples de funcionários com RandINT

from random import randint
print('precisamos sortear 1 entre os 10 funcionários do RH.')
sorteio = input("Digite qualquer coisa para iniciar o sorteio:")

num = (randint(1, 10))

if num == 1:
    print('o funcionário sorteado foi: marcelo')
elif num == 2:
    print('o funcionário sorteado foi: sonia')
elif num == 3:
    print('o funcionário sorteado foi: anderessa')
elif num == 4:
    print('o funcionário sorteado foi: eliezer')
elif num == 5:
    print('o funcionário sorteado foi: roberto')
elif num == 6:
    print('o funcionário sorteado foi: angela')
elif num == 7:
    print('o funcionário sorteado foi: tereza')
elif num == 8:
    print('o funcionário sorteado foi: mateus')
elif num == 9:
    print('o funcionario sorteado foi: manoel')
elif num == 10:
    print('o funcionario sorteado foi: jorge')
