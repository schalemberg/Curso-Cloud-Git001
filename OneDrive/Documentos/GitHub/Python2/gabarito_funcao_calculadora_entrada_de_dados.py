def calculadora(numl, num2, operacao):
    if (operacao == 1):
        return numl + num2
    elif (operacao == 2):
        return numl - num2
    elif (operacao == 3):
        return numl * num2
    elif (operacao == 4):
        return numl / num2
    else:
        return 0


executar = True
while executar:
    print("Qual operação você quer realizar?")
    print("1: Soma 2: Subtração 3: Multiplicação 4: Divisão 0: Sair")
    operacao = int(input())
    if operacao < 0 or operacao > 4:
        print("Essa opção não existe")
    elif operacao == 0:
        executar = False
    else:
        print("Insira o primeiro número da operação:")
        numl = int(input())
        print("Insira o segundo número da operação:")
        num2 = int(input())
        resultado = calculadora(numl, num2, operacao)
        print("O resultado é:", resultado)
        print("O resultado é:", resultado)
