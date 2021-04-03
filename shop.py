import xml.etree.ElementTree as ET
from GenderSwap import parse

tree = ET.parse('xmlfiles\\femalexml\\mp_f_freemode_01_mpheist4_shop.meta')
root = tree.getroot()

#print(root[6])


def hashName(index):
    for i in range(len(root[index])):
        element = root[index][i]
        nameHash = element.find('uniqueNameHash').text
        print(nameHash, '\n')

def textlabel(index):
    for i in range(len(root[index])):
        element = root[index][i]
        label = element.find('textLabel').text
        if str(label) == 'None':
            print('NULL\n')
        else:
            print(label, '\n')


def info(index):
    for i in range(len(root[index])):
        element = root[index][i]
        for n in range(len(element)):
            print(element[n].text)
        print('-----------------------------')

def test(index, keylist, valuelist):
    a = keylist
    b = valuelist
    foundhash = []
    hashlist = []

    #creates a list of data
    for i in range(len(root[index])):
        element = root[index][i]
        nameHash = element.find('uniqueNameHash').text
        hashlist.append(nameHash)
        list2 = []
        #creates the list that contains all the elements
        for n in range(len(element)):
            list2.append(element[n].text)
        #compares the two lists to find the right match
        for m in range(len(a)):
            if hashlist[i] == a[m]:
                foundhash.append(a[m])
        for l in range(len(a)):
            if list2[3] == a[l]:
                list2.append(b[l])
                print(list2)
        


'''
pedOutfits = 5
pedComponents = 6
pedProps = 7

'''


#info(7)
#textlabel(7)
p = parse('scriptmetadata', 'female')
#list1 = p.display_by_value(2900, 'female')
#print(list1)


keylist = p.display_by_ID('H4', 2, 0)
valueList = p.values(keylist)
test(7, keylist, valueList)