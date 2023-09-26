class ControleOpcoes:
    def __init__(self):
        self.itens = []

    def inserirItem(self,codigo,descricao, acrescimo,desconto, total):
        item = [codigo, descricao, acrescimo, desconto, total]
        self.itens.append(item)

    def acrescimoItem(self, codigo, acrescimo):
        for item in self.itens:
            if item[0] == codigo:
                item[2] = item[2]+acrescimo
                item[4] = item[4]+acrescimo

    def descontoItem(self, codigo, desconto):
        for item in self.itens:
            if item[0] == codigo:
                item[3] = item[3]-desconto
                item[4] = item[4]-desconto

    def acrescimoTotal(self, acrescimo):
        total = sum(item[4] for item in self.itens)
        if acrescimo > sum(item[2] for item in self.itens):
            for item in self.itens:
                proporcao_item = item[4] / total
                acrescimo_item = acrescimo * proporcao_item
                item[2] += acrescimo_item
                item[4] += acrescimo_item

        else:
            print("O valor digitado é menor do que o total dos acrescimos!")

    def descontoTotal(self, desconto):
        total = sum(item[4] for item in self.itens)

        if desconto < sum(item[3] for item in self.itens):

            for item in self.itens:
                proporcao_item = item[4] / total
                desconto_item = desconto * proporcao_item
                item[3] += desconto_item
                item[4] -= desconto_item

        else:
            print("O valor digitado é menor do que o total dos descontos!")

    def finalizarVenda(self):
        print("\nItens do Carrinho:")
        total_itens = 0
        total_acrescimo = 0
        total_desconto = 0

        for item in self.itens:
            print(f"Código: {item[0]}, Descrição: {item[1]}, Total: {item[4]}, Acréscimo: {item[2]}, Desconto: {item[3]}")

        total_itens += item[4]
        total_acrescimo += item[2]
        total_desconto += item[3]

        valor_total = total_itens + total_acrescimo - total_desconto

        print(f"\nTotal da Venda: {valor_total}")
        print(f"Desconto Total: {total_desconto}")
        print(f"Acréscimo Total: {total_acrescimo}")
        print("Venda finalizada. Obrigado!")
