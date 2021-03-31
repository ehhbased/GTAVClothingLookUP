import xml.etree.ElementTree as ET
from GenderSwap import parse

tree = ET.parse('xmlfiles\\mp_m_freemode_01_mpheist4_shop.meta')
root = tree.getroot()

#print(root[6])


def hashName(index):
    for i in range(len(root[index])):
        element = root[index][i]
        for n in range(len(element)):
            nameHash = element.find('uniqueNameHash').text
            print(nameHash, '\n')
            break


def textlabel(index):
    for i in range(len(root[index])):
        element = root[index][i]
        for n in range(len(element)):
            label = element.find('textLabel').text
            if str(label) == 'None':
                print('NULL\n')
            else:
                print(label, '\n')
            break

def info(index):
    for i in range(len(root[index])):
        element = root[index][i]
        for n in range(len(element)):
            print(element[n].text)
        print('-----------------------------')


'''
pedOutfits = 5
pedComponents = 6
pedProps = 7

'''


#info(7)
#textlabel(7)
p = parse('scriptmetadata', 'female')
list1 = p.display_by_value(2900, 'female')
print(list1)