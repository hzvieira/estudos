import statistics as st
import math as mat

# 1. Faça um Programa que peça dois números e imprima o maior deles.
def maiorNumero(num1, num2):
    return max(num1, num2)

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def sinalNumero(x):
    resultado = "Não foi possível determinar"
    if (x>0):
        resultado = "positivo"
    elif (x<0):
        resultado = "negativo"
    else:
        resultado = "numero igual a zero"
    return resultado

# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
def genero(x):
    resultado = ""
    if (x == "F"):
        resultado = "Feminino"
    elif (x == "M"):
        resultado = "Masculino"
    else:
        resultado = "Sexo Inválido"
    return resultado

# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def genero(letra):
    resultado = "Não é vogal"
    if (letra in ['a', 'e', 'i', 'o', 'u']):
        resultado = "é vogal"
    return resultado


# 5. Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
def notas(*args):
    media = st.mean(notas)
    resultado = "Aprovado com distinção"
    if (media < 7):
        resultado = "Reprovado"
    elif (media >= 7 and media < 10):
        resultado = "Aprovado"
    return resultado

# 6. Faça um Programa que leia três números e mostre o maior deles.
def maiorNumero(*num):
    return max(num)

# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
def numero(*num):
    return max(num), min(num)

# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
def menorPreco(*num):
    return min(num)

# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
def ordenacao(*num):
    return sorted(num, reverse=True)

# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
# lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
#
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
def novoSalario(antigo):
    aumento = 0
    if (antigo > 1500):
        aumento = 0.05
    elif (antigo > 700):
        aumento = 0.10
    elif (antigo > 280):
        aumento = 0.15
    else:
        aumento = 0.20

    return antigo, aumento, antigo * aumento, antigo * (1 + aumento)
