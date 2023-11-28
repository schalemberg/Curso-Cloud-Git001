def percorreLista(elem1, lista):
    encontrei = False

    for i in range(len(lista)):
        if lista[i] == elem1:
            encontrei = True

    if (encontrei == False):
        print("Não achamos o nome: " + elem1)
    else:
        print("Achamos o nome: " + elem1)


itens = ["Alexander", "Camila", "Leandro", "Gutenberg", "Heloísa"]
print("Encontramos ", itens[1], " na posição ", itens.index("Camila"))
percorreLista("Camila", itens)


"""
1- Cria uma função para percorrer um array
2- Imprimir a posicao do array
3- Perguntar para o usuário até ele encontrar o valor"""
