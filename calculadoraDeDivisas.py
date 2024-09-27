# -*- coding: utf-8 -*-


def foreign_exchange_cal(ammount): 
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Conviertes de pesos s pesos')
    print('')

    ammount = float(input('Ingresa lo que quieres convertir'))

    result = foreign_exchange_cal(ammount)
    print('${} pesos mexi son ${} pesos colom'.format(ammount, result))

if __name__ == '__main__':
    run()