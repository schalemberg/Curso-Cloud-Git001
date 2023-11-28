lista_produtos = ['máscaras faciais', 'batons', 'esmaltes',
                  'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
lista_produtos[1], lista_produtos[4] = "rímel", "creme hidratante"
lista_produtos.pop()
lista_produtos.append("creme dental")
for i in range(len(lista_produtos)):
    print("Temos", (lista_produtos)[i], "a venda.")
