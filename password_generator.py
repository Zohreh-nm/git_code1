import os
import random
import string
settings = {
    'upper': True,
    'lower': True,
    'number' : True,
    'symbol': True,
    'space' : False,
    'length' : 8,

}

def clear_screen():
    os.system('cls')
    
def get_user_password_length(option,default, min_length = 4, max_length = 8):
    while True:
        user_input = input(f'Include {option}? (default is {default}.(y: yes, n: no) Enter your password:')

        if user_input == "":
            return default
        if user_input.isdigit():
            password_length = int(user_input)
            if min_length <= password_length <= max_length:
                return int(user_input)
            print(f'Invalid input. Your pass word length should be between {min_length} and {max_length}.')
        else:
            print("Invalid input. You should enter a number.")
        print('please try again.')

def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}? (default is {default}.) (y: yes, n: no):')

        if user_input == '':
            return default
        if user_input in ['y','n']:
            return user_input == 'y'
        print("invalid input. please try again.")


def get_settings_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            password_length = get_user_password_length(option, default)
            settings[option] = password_length

def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_number():
    return random.choice('0123456789')

def get_random_symbol():
    return random.choice("""!@#$%&*'+.""")


def get_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'number':
        return get_random_number()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'space':
        return ' ' 


def password_generator(settings):
    final_password = ''
    password_length = settings['length']
    choices = list(filter(lambda x: settings[x], ['upper', 'lower', 'number', 'symbol']))

    for i in range(password_length):
        final_password += get_random_char(choices)

    return final_password

def password_regenerator(settings):
    while True:
        print('-'* 20)
        print(f"generated password : {password_generator(settings)}")
        
        while True:
            want_another_password = input('Do you want another password? (y : yes, n : no, enter: yes)')
            if want_another_password in['y', 'n', '']:
                if want_another_password == 'n':
                    return
                break
            else:
                print('invalid input. choose from:(y : yes, n : no, enter: yes).')

def run():
    clear_screen()
    get_settings_from_user(settings)
    password_regenerator(settings)
    
    

run()

    
