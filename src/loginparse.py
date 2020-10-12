import json

def getData():
    f = open('userdata.JSON')
    x = json.loads(f.read())
    f.close()

    return x['data']


def parseUser(user, password):

    userlist = getData()
    
    x = {
        'user' : user,
        'password' : password
    }

    userlist.append(x)

    data = {'data' : userlist}
    y = json.dumps(data, indent= 3)
    
    f = open("userdata.JSON", "w")
    f.write(y)
    f.close()
    print(f'New user created! Welcome {user}.')