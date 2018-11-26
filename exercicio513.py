"""
Descrição: Este programa calcula o pagamento de uma dívida.
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

mensal = 0

divida = 0

taxa = 0

n = 0

juros = 0

#Entrada de dados


divida = float(input("Qual o valor da dívida? "))

mensal = float(input("Informe o valor da parcela a pagar todos os meses: "))

taxa = float(input("Informe a taxa de juros mensal: "))

n = 0

juros = 0

#Processamento de dados

while n < 24:
    deposito = deposito + juros + mensal
    n = n + 1
    juros =  (deposito * taxa/100)
    print("O seu saldo no mês %d é de R$%5.2f e o seu rendimento total foi de R$ %5.2f" % (n, deposito, juros))


#Saída de dados

