import json
file2Open = input("Enter the filename to open: ")

def oppositeGenderFile(a):
    a = file2Open
    if file2Open != 'masks':
        if a.startswith('m'):
            return 'fe' + file2Open
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

def openFile(fileName):
    theFile = open('Jsonfiles\\' + fileName + '.json','r')
    return theFile

def printID(a, fileName):
    print("\nnumber of " + fileName + " textures: ", len(a))
    for i in range(len(a)):
        b = a[str(i)]
        print(i, "=  Text Label: ", b["GXT"], "  In-store Name: " + b["Localized"])

#opens the file
jsondata2 = openFile(oppositeGenderFile(file2Open)).read()
jsondata = openFile(file2Open).read()

#parse
obj = json.loads(jsondata)
obj2 = json.loads(jsondata2)

#prints the length of ID's found in the JSON file
if file2Open != 'masks':
    print('\n'+file2Open + ' IDs : 0 -', len(obj) - 1)
    print(oppositeGenderFile(file2Open) + ' IDs : 0 -', len(obj2) - 1)
else:
    print('\n'+file2Open[0:4] + ' IDs : 0 -', len(obj) - 1)

errorChecking = False

#checks the IDnum entered
while not errorChecking:
    IDnum = int(input("\nEnter the ID to look up: "))
    if IDnum > len(obj) or len(obj2):
        if IDnum > len(obj) and IDnum < len(obj2):
            print('the entered value is larger than what\'s found in ' + file2Open + '\n')
            mylist2 = obj2[str(IDnum)]
            printID(mylist2, oppositeGenderFile(file2Open))
            continue
        elif IDnum > len(obj) and len(obj2):
            if file2Open == 'masks':
                print('the entered value is higher than whats found in ' + file2Open)
            print('the entered value is higher than whats found in both ' + file2Open + ' and ' + oppositeGenderFile(file2Open) + '\n')
            continue
    mylist = obj[str(IDnum)]
    mylist2 = obj2[str(IDnum)]

    printID(mylist, file2Open)
    printID(mylist2, oppositeGenderFile(file2Open))
    errorChecking = True