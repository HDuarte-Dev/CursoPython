#Define uma função "para" abre espaço para uma variável

def main():
    nome = input("Qual é o seu nome?: ")
    ola()
    

def ola(para="mundo"):
    print("Olá", para)


#Executando as funções
ola()
