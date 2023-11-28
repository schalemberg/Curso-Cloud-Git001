# Receba um numero do telcado e exiba os 2 números seguintes

numero = int(input("Informe um número: "))
print(f"Os dois números seguintes são: {numero + 1} e {numero + 2}")


########## FOR ##########

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()
