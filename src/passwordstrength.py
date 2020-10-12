
import re


def error(key):
    errorlist = {
        'eight': '\tPassword is not at least eight characters',
        'lower': '\tPassword does not have a lowercase letter',
        'upper': '\tPassword does not have a uppercase letter',
        'digit': '\tPassword does not have a number',
        'symbol': '\tPassword does not have a symbol'
    } 

    error = errorlist.get(key)
    return error

def match(text):
    eightcharacters = re.compile(r'\w{8}')
    lowercase = re.compile(r'[a-z]{1}')
    uppercase = re.compile(r'[A-Z]{1}')
    containsdigit = re.compile(r'\d{1}')
    containssymbol = re.compile(r'[!@#$%^&*]{1}')

    patterns = {'eight': eightcharacters, 'lower': lowercase, 'upper': uppercase, 'digit': containsdigit, 'symbol': containssymbol}

    #   a little fun add-on that checks if the user had any errors so that we can display if they 
    #   have an acceptable password
    #   also included a strength value to show strength of password
    hasError = False
    strength = 0
    
    for key in patterns:
        if not re.search(patterns[key], text):
            print(f'\n{error(key)}') if not hasError else print(error(key))
            hasError = True        
        else:
            strength += 1
            continue

    strength =  (strength / len(patterns)) * 100

    if strength == 100:
        print('\n\tStrong password Accepted!\n')
        return True
    else:
        print(f'\tPassword is %{strength} strong!\n')
        return False

if __name__ == "__main__":
    while True:
        password = input("Enter password: ")
        match(password)


