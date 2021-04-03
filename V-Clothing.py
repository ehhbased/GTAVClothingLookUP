import json

class jsonparse:
    def __init__(self, file2open, OGF):
        self.filename = file2open
        self.OGF = OGF
    
    def openFile(self):
        theFile = open('Jsonfiles\\' + self.filename + '.json','r')
        return theFile
    
    def openOppFile(self):
        theFile = open('Jsonfiles\\' + self.OGF + '.json','r')
        return theFile

    def printID(self, a, IDnum):
        print("\nnumber of " + self.filename + " textures: ", len(a))
        for i in range(len(a)):
            b = a[str(i)]
            print(str(IDnum) + ' -', i, "=  Text Label: ", b["GXT"], "  In-store Name: " + b["Localized"])


def oppGenderFile(a):
    a = file2open
    if file2open != 'masks':
        if a.startswith('m'):
            return 'fe' + file2open
        elif a.startswith('f'):
            b = a.split('_')
            b[0] = 'male'
            return b[0] + '_' + b[1]
        elif a[6] == 'f':
            c = a.split('_')
            c[1] = 'male'
            return c[0] + '_' + c[1] + '_' + c[2]
        elif a[6] == 'm':
            d = a.split('_')
            d[1] = 'female'
            return d[0] + '_' + d[1] + '_' + d[2]
    else:
        return a

def checklength(filename, obj, obj2):
    #prints the length of ID's found in the JSON file
    if filename != 'masks':
        print('\n   > '+filename + ' IDs : 0 -', len(obj) - 1)
        print('   > '+ oppGenderFile(file2open) + ' IDs : 0 -', len(obj2) - 1)
    else:
        print('\n   > '+filename[0:4] + ' IDs : 0 -', len(obj) - 1)

#checks the IDnum entered
def run():
    errorChecking = False
    while not errorChecking:
        IDnum = int(input("\n------------------------------\nEnter the ID to look up: "))
        if IDnum > len(obj) or len(obj2):
            if IDnum > len(obj) and IDnum < len(obj2):
                print('the entered value is larger than what\'s found in ' + file2open + '\n')
                mylist2 = obj2[str(IDnum)]
                p.printID(mylist2, IDnum)
                continue
            elif IDnum > len(obj2) and IDnum < len(obj):
                print('the entered value is larger than what\'s found in ' + oppGenderFile(file2open) + '\n')
                mylist = obj[str(IDnum)]
                p.printID(mylist, IDnum)
                continue
            elif IDnum > len(obj) and len(obj2):
                if file2open == 'masks':
                    print('the entered value is higher than whats found in ' + file2open)
                print('the entered value is higher than whats found in both ' + file2open + ' and ' + oppGenderFile(file2open) + '\n')
                continue
        if file2open != 'masks':
            mylist = obj[str(IDnum)]
            mylist2 = obj2[str(IDnum)]

            p.printID(mylist, IDnum)
            p.printID(mylist2, IDnum)
            errorChecking = True
        else:
            mylist = obj[str(IDnum)]
            p.printID(mylist, IDnum)


if __name__ == '__main__':
    file2open = input("Enter the filename to open: ")
    p = jsonparse(file2open, oppGenderFile(file2open))

    #opens the file
    jsondata = p.openFile().read()
    jsondata2 = p.openOppFile().read()

    #parse
    obj = json.loads(jsondata)
    obj2 = json.loads(jsondata2)

    checklength(file2open, obj, obj2)

    run()