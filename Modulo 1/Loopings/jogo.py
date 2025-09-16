import random 

print ("bem_vindo ao jogo adivinhaçao!")

segredo = random.randint(1, 10)
palpite = 0
tentativas = 0

while palpite!= segredo:
  try:
      palpite = int(input("tente adivinhar o numero 1 a 10: "))
      tentativas +=1
      if palpite < segredo:
          print("mais!")
      elif palpite > segredo:
          print("menos!")
       
  except ValueError:
      print("por favor digite um numero valído")

print("parábens!você acertou o número {segredo} em {tentativa} tentativa(s)!")