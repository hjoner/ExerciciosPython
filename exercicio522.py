"""
Descrição: Este programa demonstra as operações informadas pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:01/12/2018
"""

#Inicialização de variáveis


operacao = 0

x = 0

tabuada = 0

#Entrada de dados

while True:
    
    operacao = input("Informe a operação desejada: adição (+), subtração (-), divisão (/), multiplicação (*) ou tecle sair para encerrar. ")

    x = 1
    
    if operacao == "sair":
        break
        
    elif operacao != "+" or "-" or "/" or "*":
        tabuada = int(input("Digite o número que deseja obter a tabuada "))
        X = 1
        
#Processamento de dados        
        while x<=10:
            
            if operacao == "+":
                print("%d + %d é %d" % (tabuada, x, x + tabuada))
            elif operacao == "-":
                print("%d - %d é %d" % (tabuada, x, x - tabuada))
            elif operacao == "*":
                print("%d * %d é %d" % (tabuada, x, x * tabuada))
            elif operacao == "/":
                print("%d / %d é %d" % (tabuada, x, x / tabuada))    
            x += 1
    else:
        print("Erro! Você deve escolher uma opção válida!")


#Saída de dados

