from random import randint

quantidade_total = int(input("Quantidade total de funcionários: "))
quantidade_sorteio = int(input("Quantidade de pessoas a serem sorteadas: "))


funcionarios = [
    'marcelo', 'sonia', 'anderessa', 'eliezer', 'roberto',
    'angela', 'tereza', 'mateus', 'manoel', 'jorge'
]

if quantidade_sorteio > quantidade_total:
    print("A quantidade de pessoas a serem sorteadas não pode ser maior que a quantidade total de funcionários.")
else:
    # Realiza o sorteio
    print('Funcionários sorteados:')
    for _ in range(quantidade_sorteio):
        num = randint(0, quantidade_total - 1)
        print(f"O funcionário sorteado foi: {funcionarios[num]}")
u
