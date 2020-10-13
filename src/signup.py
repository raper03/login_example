import src.passwordstrength as passwordstrength
import pyinputplus as pyip

from src.loginparse import loginparse as parse
signupparse = parse()

def newuser():
    dicti = signupparse.getData()

    while True:
        yesVal = 'yes'
        user = pyip.inputStr('\tPlease enter a username: ')

        result = True
        for dictis in dicti:
            if dictis['user'] == user:
                print(f'{user} is already taken!')
                result = False
                break
            else:
                continue

        if result:
            choice = pyip.inputYesNo(f'Desired username is: {user}? ', yesVal= yesVal )
            if choice == yesVal:
                return user      
            else:
                continue
                    
        

def newpassword():
    while True:
        password = pyip.inputStr('\tPlease enter user password: ',strip = ' ')
        result = passwordstrength.match(password)
        if not result:
            continue
        else:
            return password

    
def prompt():
    
    print('Create an account:')
    user = newuser()
    password = newpassword()
    
    signupparse.parseUser(user, password)
    return
    

    
    
        

    



