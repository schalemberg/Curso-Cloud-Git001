# saldo = 500
# print(f'Saldo Atual: {saldo}')
# valor_saque = input ('Informe o valor do seu saque:')


# AND = para ser verdadeiro, todas as condições precisam ser verdadeiras
# OR = para ser verdadeiro, pelo menos uma condição precisa ser verdadeira
# NOT = para ser verdadeiro, a condição precisa ser falsa

# Operador E, OU
saldo = 1000
saque = 500
limite = 100
saldo >= saque and saque <= limite
saldo >= saque or saque <= limite

# Operador de negação

contatos_emergencia = []

not 1000 > 1500
not contatos_emergencia

saldo = 1000
saque = 500
limite = 100
conta_especial = True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

# Operadores de identidade

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200
curso is nome_curso
print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)

# Operadores de associação

curso = "Curso de Python"
fruta = ["maça", "banana", "uva"]
saques = [1500, 500, 1000]

"Python" in curso
print("Python" in curso)
"banana" not in fruta
print("maça" in fruta)
200 in saques
print(200 in saques)
