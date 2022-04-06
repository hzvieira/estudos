import statistics as st
import math as math

# 2. Faça um Programa que peça um número e então mostre 
# a mensagem O número informado foi [número].
# print("o numero informado foi: ", input("Digite um número: "))

# 3. Faça um Programa que peça dois números e imprima a soma.
"""
def somar(num1, num2):
    return (num1 + num2)

num1 = int(input("Digite um primeiro número: "))
num2 = int(input("Digite um segundo número: "))

print("A soma é: ", somar(num1, num2))
"""

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = [10, 9, 9, 8]
print(st.mean(notas))

# 5. Faça um Programa que converta metros para centímetros.
def transformCentimetros(metros):
    return metros / 1000

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calcularAreaCirculo(raio):
    return (math.pi * raio**2)

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def areaQuadrado(base, altura):
    return base * altura

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
def custoHora(salario, horasTrabalhadas):
    return salario / horasTrabalhadas

# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
def fahrenheitToCelsius(fahrenheit):
    return 5 * ((fahrenheit - 32) / 9)

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
""" 
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""
def calculos(int1, int2, float1):
    a = (int1 * 2) * (int2 /2)
    b = (int1 * 3) + float1 
    c = float1**3
    
    return

# 13. Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7
def pesoIdealHomem(altura):
    return (72.7*altura) - 58

def pesoIdealMulher(altura):
    return (62.1*altura) - 44.7

#14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso 
# (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável 
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
def pesca(quilos):
    tetoRegulamento = 50
    if (quilos <= tetoRegulamento):
        multa = 0
    elif (quilos >= (tetoRegulamento * 2)):
        multa = tetoRegulamento + (quilos % tetoRegulamento)
    return multa

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
# 11% para o Imposto de Renda, # 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo: 
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
def salarioLiquido(salarioBruto):
    ir = salarioBruto * 0.11
    inss = salarioBruto * 0.08
    sindicato = salarioBruto * 0.05

    return salarioBruto - (ir + inss + sindicato)

# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
def gastoDeTinta(metros):
    latas = math.ceil(metros / 54)
    valor = latas * 80
    return  [latas, valor]

# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a. comprar apenas latas de 18 litros;
# b. comprar apenas galões de 3,6 litros;
# c. misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
def gastoDeTintaLatas(metros):
    latas = math.ceil(metros / 108)
    valor = latas * 80
    return  [latas, valor]

def gastoDeTintaGaloes(metros):
    galoes = math.ceil(metros / 21.6)
    valor = galoes * 25
    return  [galoes, valor]

def gastoDeTintaGaloes(metros):
    galoesSemDesperdicio = 0

    litros = (metros / 6) * 1.1
    latasSemDesperdicio = math.floor(litros / 18)
    sobra = litros % 18
    if (sobra >= 11.52):
        latasSemDesperdicio+= 1
    else:
        galoesSemDesperdicio = math.ceil(sobra / 3.6)

    valor = (latasSemDesperdicio * 80) + (galoesSemDesperdicio * 25)

    return  [latasSemDesperdicio, galoesSemDesperdicio, valor]


# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em segundos).
def calculaVelocidade(mb, velocidade):
    mb = 50
    velocidade = 10

    tempo = (mb / 10) / 60
    return 60 * tempo

input("Tecle [enter] pra fechar")

