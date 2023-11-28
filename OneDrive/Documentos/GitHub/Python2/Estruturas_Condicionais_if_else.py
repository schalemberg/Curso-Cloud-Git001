########## Estruturas condicionais ##########
# IF
saldo = 500
print(f'Saldo Atual: {saldo}')
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print("Valor sacado: ", saque)
    saldo -= saque
    print(f'Novo saldo: {saldo}')

if saque > saldo:
    print("Saldo insuficiente!")
    print(f'Saldo Atual: {saldo}')


######### ELSE ###############

saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print("Valor sacado: ", saque)
    saldo -= saque
    print(f'Novo saldo: {saldo}')
else:
    print("Saldo insuficiente!")
    print(f'Saldo Atual: {saldo}')

############# ELIF #############

opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato "))

saldo = 2000
if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    print("Saque realizado com sucesso!")
    print(f"Seu saldo atual é {saldo - valor}")
elif opcao == 2:
    print(f"Extrato = {saldo}")
else:
    print("Opção inválida!")

############# IF ANINHADO #############
conta_normal = True
conta_universitaria = False
saldo = 1000
saque = 3500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saldo <= (saldo + cheque_especial):
        print("Saldo realizado com o uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")


############# OPERADOR TERNÁRIO #############

saldo = 500
saque = 200
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
