# Como funciona um input e uma variável em Python
nome = input("Qual é o seu nome?: ")
idade = input("Qual a sua idade?: ")

# Referenciar uma variável
# Concatenação
#V1

#print("Olá " + nome + ", você tem " +idade+ " anos de idade !")

#Concatenação V2
#Parâmetros de um Print
#End se refere ao que aparecerá após um Print
"""
print("Olá ", "", end="" )
print(nome,"", end="")
print("Sua idade é de", "", end="")
print(idade,"", end="" )
print("anos !!")
"""
#V3
#Remover espaços e Capitalizar
#Pode ser feito diretamente no Input

nome = nome.strip().title()
idade = idade.strip()

print("Olá " + nome + ", você tem " +idade+ " anos de idade !")

