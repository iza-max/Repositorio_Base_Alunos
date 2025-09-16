numero = int(input("digite um numero: "))
inicio = int(input("digite onde vai começar: "))
fim = int(input("digite onde vai terminar: "))

while inicio <= fim:
    print(f"{inicio} x {numero} = {inicio * numero}")
    inicio +=1
