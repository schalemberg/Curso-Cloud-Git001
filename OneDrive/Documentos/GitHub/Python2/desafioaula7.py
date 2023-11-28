def controle_estoque(lista_produtos):
    for produto in lista_produtos:
        print("Temos", produto, "a venda")


# lista os produtos disponíveis no estoque
lista_produtos = ['arroz', 'feijão', 'legumes',
                  'carnes', 'sabonete', 'café', 'chocolate', 'leite']
# faz alterações na lista dos produtos
lista_produtos[1], lista_produtos[4] = "creme dental", "lasanha"
controle_estoque(lista_produtos)
