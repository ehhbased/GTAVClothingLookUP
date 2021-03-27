import json
print('''
* human readable names of GTA V clothing items.

* Many items have "NO_LABEL" and "NULL" as their names, which probably means they aren't available for purchase in GTA Online clothes shops
OR they're old enough to have their names hardcoded in game scripts.

* Files without a prefix (e.g. masks.json) are the clothing items for both mp_m_freemode_01 and mp_f_freemode_01 models.

* Files prefixed with male_ are the clothing items for mp_m_freemode_01 model. (male character)

* Files prefixed with female_ are the clothing items for mp_f_freemode_01 model. (female character)

* Files prefixed with props_male_ are the props for mp_m_freemode_01 model. (male props ie. glasses, watch, ears, bracelets)

* Files prefixed with props_female_ are the props for mp_f_freemode_01 model. (female props ie. glasses, watch, ears, bracelets)

''')
file2Open = input("Enter the file to open: ")
#opens the file
FILE = open('Jsonfiles\\' + file2Open + '.json','r')
jsondata = FILE.read()

#parse 
obj = json.loads(jsondata)
IDnum = int(input("Enter the ID to look up: "))
mylist = obj[str(IDnum)]
print("number of textures: ", len(mylist))

for i in range(len(mylist)):
    list2 = mylist[str(i)]
    print(i, "=  Code Name: ", list2["GXT"], "  In-store Name: " + list2["Localized"])