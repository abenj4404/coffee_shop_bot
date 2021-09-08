# IMPORT OUTSIDE FUNCTIONS FROM UTILS.PY FILE
from utils import print_message, get_size, order_latte

# FUNCTIONS
def coffee_bot():
    name = input('Can I get your name please? \n> ')
    print('Hi, {}! Welcome to the cafe.'.format(name))
    order_drink = 'y'
    drinks = ['']

    while order_drink == 'y':
        size = get_size()
        drink_type = get_drink_type()
        drink = '{} {}'.format(size, drink_type)
        print('Alright, that\'s a {}!'.format(drink))
        drinks.append(drink)

        while True:
            order_drink = input('Would you like to order another drink? (y/n)')
            if order_drink in ['y', 'n']:
                break

    print('\nOkay, you\'ve ordered:')
    for drink in drinks:
        print(drink)
    print('\nYour order will be ready shortly!')

def get_drink_type():
    res = input('Got it. What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return order_mocha()
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

def order_mocha():
    while True:
        res = input('Would you like to try our limited-edition peppermint mocha? [a] Sure! [b] Maybe next time!')
        if res == 'a':
            return 'peppermint mocha'
        else:
            return 'regular mocha'

# CALL COFFEE BOT
coffee_bot()

