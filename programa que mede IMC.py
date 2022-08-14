import time
import math
print('\tSeja bem vindo(a) ao cálculo de IMC!\n')

loop = 0
time.sleep(2)

print('ATENÇÃO, É IMPORTANTE SABER:\nAbaixo de 18,5: Baixo peso.\nEntre 18,5 e 25,0: Peso normal\nEntre 25,0 e 30,0: Sobrepeso.\nAcima de 30,0: Obesidade.\n')

time.sleep(2)
altura = float(input('Digite a sua altura em metros (ex: 1.74): '))
peso = float(input('Digite o seu peso: '))
imc = (peso / (pow(altura,2)))
print('\t CALCULANDO...\n')

time.sleep(2)

print('\t O seu índice de massa corporal é {:.2f}!\n'.format(imc))

def result():
    if imc < float(18.5):
        print('Você está abaixo do peso ideal.')
    elif imc > 18.5 and imc < 25:
        print('Você está no peso ideal!')
    elif imc > 25 and imc < 30:
        print('Você está acima do peso ideal.')
    elif imc > float(30):
        print('Você está obeso.')
result()

