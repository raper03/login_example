import json

class loginparse:
    def __init__(self, directory = r'src\userdata.JSON'):
        self.directory = directory

    def getData(self):

        f = open(self.directory)
        x = json.loads(f.read())
        f.close()

        return x['data']

    def setData(self, data):
        y = json.dumps(data, indent= 3)

        f = open(self.directory, "w")
        f.write(y)
        f.close()

    def parseUser(self, user, password):

        userlist = self.getData()
        
        x = {
            'user' : user,
            'password' : password
        }

        userlist.append(x)

        data = {'data' : userlist}
        self.setData(data)
        print(f'New user created! Welcome {user}.')

