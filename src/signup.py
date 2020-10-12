import passwordstrength
import pyinputplus as pyip
import loginparse as parse

def newuser():
    dicti = parse.getData()

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
    parse.parseUser(user, password)
    return
    

    
    
        

    



