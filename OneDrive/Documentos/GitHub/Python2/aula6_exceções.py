# Tratamento de erros

def mostrarNumero():  # definição da função
    print("Escreva um número menor que 100: ")

    numero_valido = False  # variavel booleana

    while (numero_valido == False):  # loop
        try:  # tratamento de erro
            numero = int(input())  # entrada de dados
            if (numero > 100):  # condição
                print("O número não é menor que 100")  # saída de dados
            if (numero < 0):  # condição
                print("O número é menor que zero")  # saída de dados
            else:
                print("Você digitou o número: " + str(numero))
                numero_valido = True  # variavel booleana
        except:  # tratamento de erro
            print("Você não digitou um número válido")


  # chamada da função
mostrarNumero()


def numero_par():
    print("Escreva um número par: ")
    numero_par = False
    while (numero_par == False):
        try:
            numeroPar = int(input())
            if (numeroPar % 2 == 0):  # condição
                print("O número é divisível por 2")
            if (numeroPar % 3 == 0):  # condição
                print("O número é divisível por 3")
            if (numeroPar % 2 != 0 and numeroPar % 3 != 0):  # condição
                print("O número não é válido")
                numero_par = True
        except:
            print("Você não digitou um número válido")


numero_par()

# verificar se o numero é menor que 0 e lancar um erro pra ele
# criar uma segunda função que recebe um numero para ser verificado
# pedir um numero que seja divisivel por 2 e 3
