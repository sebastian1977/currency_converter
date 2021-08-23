from os import system
from msvcrt import getch
def currency_converter():
    system('cls')
    currency_dict = {'GBP':0.73,'EUR':0.86,'NOK':9.09,'PLN':3.94,'RUB':74.28,'GOLD':0.015}
    quantity = input('Enter the amount to convert or press CTRL + Z to break the program: ')
    
    print('\nAvailable currencies:\n')
    for currency_list in currency_dict:
        print(currency_list)
    choice = input('\nChoice currency for conversion: ').upper()
    if choice in currency_dict:
        result = int(quantity) * currency_dict[choice]
        print(f'\n{quantity} United States Dollars will give you {result} {choice}\n')
        print('Press spacebar.\n')
        getch()
        currency_converter()
    else:
        print('Something went wrong. Press spacebar to try again.')
        getch()
        currency_converter()
currency_converter()
