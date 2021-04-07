import xml.etree.ElementTree as ET
import os
import VClothing
import json


def xmlsearch(labelstr, index):
    directory = 'xmlfiles\\malexml\\'
    malestr = labelstr[index]
    found = []

    for filename in os.listdir(directory):
        if filename.endswith('.meta'):
            #print(os.path.join(directory, filename))
            tree = ET.parse(directory + filename)
            root = tree.getroot()
            for u in range(len(root)):
                for i in range(len(root[u])):
                    element = root[u][i]
                    label = element.find('textLabel').text
                    hasher = element.find('uniqueNameHash').text
                    if label == malestr:
                        found.append(label)
                        found.append(hasher)
    return found

def scriptmetasearch(matchlist):
    val2comp = []
    keysfound= []

    tree = ET.parse('xmlfiles\\scriptmetadata.meta')
    root = tree.getroot()
    for i in range(len(root[2])):
        element = root[2][i]
        for u in element.findall('Item'):
            key = u.get('key')
            value = u.get('value')
            for a in range(len(matchlist)):
                if key == matchlist[a]:
                    val2comp.append(value)
        
    for i in range(len(root[2])):
        ment = root[2][i]
        for c in ment.findall('Item'):
            key2 = c.get('key')
            value2 = c.get('value')
            for d in range(len(val2comp)):
                if value2 == val2comp[d]:
                    m = key2.split('_')
                    #converts female mask to male mask
                    if m[4] == 'BERD':
                        m[3] = 'M'
                        strl = '_'
                        n = strl.join(m)
                        keysfound.append(n)
                    else:
                        keysfound.append(key2)
    
    return keysfound

def idek(fvck, match):
    filterlist = []
    found = []
    for filename in os.listdir('xmlfiles\\malexml\\'):
        if filename.endswith('.meta'):
            tree = ET.parse('xmlfiles\\malexml\\' + filename)
            root = tree.getroot()
            for u in range(len(root)):
                for i in range(len(root[u])):
                    element = root[u][i]
                    label = element.find('textLabel').text
                    hasher = element.find('uniqueNameHash').text
                    for a in range(len(fvck)):
                        if hasher == fvck[a]:
                            filterlist.append(label)
    for a in range(len(filterlist)):
        for i in range(len(match)):
            if match[i].startswith('D'):
                continue
            elif match[i] == filterlist[a]:
                continue
            found.append(filterlist[a])
    found = list(set(found))
    return found

def result(a):
    directory = 'Jsonfiles\\'
    lista = a
    for i in range(len(lista)):
        for filename in os.listdir(directory):
            #print(directory + filename)
            data = open(directory + filename, 'r')
            jsonobj = json.load(data)
            for a in range(len(jsonobj)):
                data = jsonobj[str(a)]
                ID = a
                for b in range(len(data)):
                    data2 = data[str(b)]
                    texture = b
                    #print(ID, texture)
                    if data2["GXT"] == lista[i]:
                        print(filename)
                        print('ID:', ID, 'Texture:', texture)
                        print(data2["Localized"])


print(
'''
What does this tool do? : 
 > tool that makes it easiy to view a specific ID texture on the opposite Gender

 > tool that also makes it easy to look up what unlocks what using the genderswap glitch
 
 CATEGORIES:

 - accessories  - hair      - legs
 - shoes        - tops      - torso 
 - undershirts  - bracelets - ears
 - glasses      - hats      - watches
 - masks
'''
)


popen = str(input("Enter the category to open: "))
print('\n-------------------------------------------\n')
j = VClothing.jsonparse(popen)

print('\n-------------------------------------------')
print('**GENDERSWAP**\n')
gen = str(input("Choose the gender: "))
index = int(input("Enter texture num to look up: "))

if gen == 'male':
    tfound = j.mtexturesfound
elif gen == 'female':
    tfound = j.ftexturesfound

#searches the xml files for the keys needed to compare
match = xmlsearch(tfound, index)
#print(match)

#takes the keys found and returns matches found in the scriptmeta file
scriptsearch = scriptmetasearch(match)
print(scriptsearch)

#returns a list of textlabels that  we will look for in the json files for
oppgender = idek(scriptsearch, match)
print(oppgender)
print('\n-------------------------------------------\n')
result(oppgender)