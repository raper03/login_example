import loginparse as parse
import pyinputplus as pyip

def enter(value):
    key = pyip.inputStr(prompt = f'\tPlease enter {value}: ')
    return key

def check(user, password):
    dicti = parse.getData()
    
    for index in range(len(dicti)):
        if dicti[index]['user'] == user and dicti[index]['password'] == password:
            print('Signed in!')
            return True
        else:
            continue

    print('Can\'t find account or incorrect password')
    return False


def prompt():
    print('Log in to your account:')
    checking = True
    attempts = 0
    while checking:
        if attempts > 2:
            print('Too many login attempts, kicking out!')
            checking = False

        user = enter('username')
        password = enter('password')    
        validation = check(user,password)

        if validation == True:
            #TODO - create club penguin
            print('You may now play club penguin')
            checking = False
        else:
            attempts += 1
            continue

    return