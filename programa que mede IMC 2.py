import time
import math

print('\tSeja bem vindo(a) ao cálculo de IMC!\n')
time.sleep(1)

print('ATENÇÃO, É IMPORTANTE SABER:\nAbaixo de 18,5: Baixo peso.\nEntre 18,5 e 25,0: Peso normal\nEntre 25,0 e 30,0: Sobrepeso.\nAcima de 30,0: Obesidade.\n')
time.sleep(1)

def imc():
    altura = float(input('Digite a sua altura em metros (ex: 1.74): '))
    peso = float(input('Digite o seu peso: '))
    calc_imc = (peso / (pow(altura, 2)))
    print('\n\tCALCULANDO...\n')
    time.sleep(1)
    print('\tO seu índice de massa corporal é {:.2f}!\n'.format(calc_imc))
    def result():
        if calc_imc < float(18.5):
            print('Você está abaixo do peso ideal.')
        elif calc_imc > 18.5 and calc_imc < 25:\
            print('Você está no peso ideal!')
        elif calc_imc > 25 and calc_imc < 30:\
            print('Você está acima do peso ideal.')
        elif calc_imc > float(30):\
            print('Você está obeso.')
    result()
imc()
time.sleep(1)
def novamente():
    resp = input('\nDeseja refazer o cálculo? digite sim ou não: ')
    while resp in (resp):
        if resp == 'sim':
            imc(), novamente()
            break
        else:
            print('\nObrigado por usar nosso programa!')
            break

novamente()


