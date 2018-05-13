objects = []
serials = ['1234','2345']
names = ['object1', 'object2']
comnames = ['comname1','comname1']

class object():
    def __init__(self,num,name,comname):
        self.number = num
        self.name = name
        self.comname = comname
        objects.append(self)

for i in range(len(serials)):
    i = object(serials[i],names[i],comnames[i])

search = input('enter serial\n')
for object in objects:
    if object.number == search:
        print('yes')
