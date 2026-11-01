from time import sleep

produtos = [
      {"ID":1,"nome":"Notbook", "preco": 3500.00},
      {"ID":2,"nome":"Mouse", "preco": 80.00},
      {"ID":3,"nome":"Teclado", "preco": 150.00},
      {"ID":4,"nome":"Fones de ouvido", "preco": 90.00},
      {"ID":5,"nome":"Cadeira Gamer", "preco": 180.00},
      {"ID":6,"nome":"Caderno", "preco": 30.00},
]
carrinho = []
def mostrar_produtos():
    print("\n\033[31m==PRODUTOS DISPONIVEIS==\033[m")
    print('cod | produto| preço')
    for p in produtos:
        print(f'{p['ID']:<3}|{p['nome']:<10}|R${p['preco']:.2f}')


def adicionar_ao_carrinho():
    mostrar_produtos()
    try:
        codigo = int(input('Digite o ID do produto: '))

        produto_encontrado = None
        for p in produtos:
            if p['ID'] == codigo:
                produto_encontrado = p
                break
        if produto_encontrado:
            quantidade = int(input('Quantidade: '))

            item = {
                "nome":produto_encontrado["nome"],
                "preco":produto_encontrado["preco"],
                "quantidade":quantidade
            }
            carrinho.append(item)
            print(f'\n{produto_encontrado["nome"]} adicionado com sucesso!')
        else:
            print('Produto não encontrado.')
    except ValueError:
        print('\033[31mPor favor didite um valor válido.\033[m')


def visualizar_carrinho():
    if not carrinho:
        print('Carrinho vazio!')
        return
    print('\n\033[34m  ITENS NO CARINHO  \033[m')
    total = 0

    for i, item in enumerate(carrinho, start=1):
        subtotal = item["preco"] * item["quantidade"]
        total += subtotal
        print(f'\n{i}. {item["nome"]} - {item["quantidade"]} X R$ {item["preco"]:.2f} = {subtotal:.2f}')
    print(f'\nTOTAL: R${total:.2f}')


def finalizar_compra():
    visualizar_carrinho()
    if carrinho:
        print('Compra finalizada com sucesso. Muita obrigada(o)!')
        carrinho.clear()

while True:
    print('\033[1;35m\n===LOJINHA VIRTUAL===\033[m')

    print('1-Ver produtos')
    print('2-Adicionar ao carrinho')
    print('3-Finalizar compra')
    print('4-Ver Carinho')
    print('5-Sair da Lojinha')
    sleep(1)
    print()

    try:
        opc = int(input("Escolha sua opção: "))
    except ValueError:
        print('\n\033[31mERRO! Digite um numero válido.\033[m')
        continue

    if opc == 1:
        mostrar_produtos()
    elif opc == 2:
        adicionar_ao_carrinho()
    elif opc == 3:
        finalizar_compra()
    elif opc ==4:
        visualizar_carrinho()
    elif opc == 5:
        print('Encerrando programa...')
        sleep(1)
        break
    else:
        print('Opção inválida!')