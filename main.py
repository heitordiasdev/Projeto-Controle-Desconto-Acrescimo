from controleOpcoes.controleOpcoes import ControleOpcoes

controle = ControleOpcoes()

while True:
    print("\nMenu:")
    print("1. Inserir item ao carrinho")
    print("2. Acréscimo de item")
    print("3. Desconto de item")
    print("4. Acréscimo total")
    print("5. Desconto total")
    print("6. Finalizar venda")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        codigo = input("Digite o código do item: ")
        descricao = input("Digite a descrição do item: ")
        acrescimo = float(input("Digite o valor do acréscimo: "))
        desconto = float(input("Digite o valor do desconto: "))
        total = float(input("Digite o valor total: "))
        controle.inserirItem(codigo, descricao, acrescimo, desconto, total)
    elif escolha == '2':
        codigo = input("Digite o código do item: ")
        acrescimo = float(input("Digite o valor do acréscimo: "))
        controle.acrescimoItem(codigo, acrescimo)
    elif escolha == '3':
        codigo = input("Digite o código do item: ")
        desconto = float(input("Digite o valor do desconto: "))
        controle.descontoItem(codigo, desconto)
    elif escolha == '4':
        valor_acrescimo_total = float(input("Digite o valor do acréscimo total: "))
        controle.acrescimoTotal(valor_acrescimo_total)
    elif escolha == '5':
        valor_desconto_total = float(input("Digite o valor do desconto total: "))
        controle.descontoTotal(valor_desconto_total)
    elif escolha == '6':
        controle.finalizarVenda()
    elif escolha == '7':
        print("Saindo. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

