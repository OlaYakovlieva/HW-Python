print("Welcome to the restaurant 'Monti'!")
import random
menu = input("Please, enter what would you like for dinner using comma: \n" ).split(",")
print('-------"Monti"-------') 
for item in menu:
    print(f'{item}............{random.randint(10,50)} hrn' )
print("...\n" f'all............{random.randint(50,150)} hrn')
