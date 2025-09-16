nome = input("digite seu nome:")
peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

IMC = peso/(altura**2)

if IMC < 18.5:
    print("abaixo do peso")
elif IMC < 24.9:
    print("peso normal")
elif IMC < 29.9:
    print("sobrepeso")
elif IMC < 34.9:
    print("obesidade grau |")
elif IMC <39.9:
    print("obesidade grau||")   
else:
    print("obesidade grau|||")

print(F"o IMC do paciente {nome} e {IMC:.2f}")






