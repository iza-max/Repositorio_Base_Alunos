nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
carteira =input ("possui carteira? (1-sim | 2-não)")


if idade >=18:

    print("maior de idade")
    if carteira == "1":
        print("pode dirigir ✅")
    else:
        print("não pode dirigir ❌")
else:
    print("menor de idade🔞")
