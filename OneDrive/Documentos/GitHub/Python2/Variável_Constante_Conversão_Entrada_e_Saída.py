print("Hello word!")

# exemplo de uma VARIÁVEL com dois valores diferentes
nome = 'Guilherme'
idade = 28

nome, idade = 'Giovanna', 27
print(f'Meu nome é {nome} e eu tenho {idade} ano(s) de idade.')

# -----exemplo de uma CONSTANTE
DEBUG = True
BRAZILIAN_STATES = [
    'SP',
    'RJ',
    'MG'
]
print(BRAZILIAN_STATES)

# ------Exemplo de conversao inteiro para float
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)

# ------Exemplo de conversao float para inteiro

preco = 10.30
print(preco)

preco = int(preco)
print(preco)

# ------Exemplo de conversão por divisão

preco = 10
print(preco)

print(preco / 2)

print(preco // 2)

# -----Exemplo de numérico para string

preco = 10.50
idade = 28
print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

# -----Exemplo de string para numero

preco = "10.50"
idade = '28'
print(float(preco))

print(int(idade))

# -----Exemplo de Entrada

nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')
print(f'Seu nome é {nome} e você possui {idade} anos.')

# Exemplo de saída
nome = 'Guilherme'
sobrenome = 'Carvalho'

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")
