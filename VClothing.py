import json
import os

class jsonparse:
    def __init__(self, var):
        directory = 'Jsonfiles\\'

        self.ftexturesfound = []
        self.mtexturesfound = []

        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                variations = filename.split('.')[0]
                listsplit = variations.split('_')
                backward = listsplit[::-1]
                if backward[0] == 'masks' and var == 'masks':
                    self.maskpath = directory + filename
                    self.maskdir = backward[0]
                elif backward[0] == var and backward[1] == ('male'):
                    self.mpath = directory + filename
                    self.mdir = backward[1]
                elif backward[0] == var and backward[1].startswith('f'):
                    self.fpath = directory + filename
                    self.fdir = backward[1]

        

        if var == 'masks':
            maskdata = open(self.maskpath, 'r')
            self.maskJsonObj = json.load(maskdata)
            print('     >',self.maskdir, len(self.maskJsonObj))
            print('\n-------------------------------------------\n')
            IDnum = int(input("Enter the ID to look up: "))
            if IDnum < len(self.maskJsonObj):
                self.outputID(IDnum, 'masks')
            else:
                print('the entered value is higher than whats found in ' + self.maskdir)
        else:
            maledata = open(self.mpath, 'r')
            femaledata = open(self.fpath, 'r')
            #parses the json files and loads them as a dictionary
            self.mJsonObj = json.load(maledata)
            self.fJsonObj = json.load(femaledata)

            print('     >',self.mdir, len(self.mJsonObj))
            print('     >',self.fdir, len(self.fJsonObj))
            print('\n-------------------------------------------\n')
            IDnum = int(input("Enter the ID to look up: "))

            if IDnum < len(self.mJsonObj) and IDnum < len(self.fJsonObj):
                self.outputID(IDnum, 'male')
                self.outputID(IDnum, 'female')
            elif IDnum > len(self.mJsonObj) or len(self.fJsonObj):
                #bigger than male and less than female
                if IDnum > len(self.mJsonObj) and IDnum < len(self.fJsonObj):
                    print('the entered value is larger than what\'s found in ' + self.mdir + '\n')
                    self.outputID(IDnum, 'female')
                
                #bigger than female and less than male
                elif IDnum > len(self.fJsonObj) and IDnum < len(self.mJsonObj):
                    self.outputID(IDnum, 'male')
                    print('\n\nthe entered value is larger than what\'s found in ' + self.fdir + '\n')
                
                #bigger than both male and female
                elif IDnum > len(self.mJsonObj) and len(self.fJsonObj):
                    print('the entered value is higher than whats found in both ' + self.mdir + ' and ' + self.fdir + '\n')

    
    def outputID(self, IDnum, gender):
        if gender == 'male':
            self.mtexturelist = self.mJsonObj[str(IDnum)]

            print("\nnumber of " + self.mdir + " textures: ", len(self.mtexturelist))
            for i in range(len(self.mtexturelist)):
                b = self.mtexturelist[str(i)]
                print(str(IDnum) + ' -', i, "=  Text Label: ", b["GXT"], "  In-store Name: " + b["Localized"])
                self.mtexturesfound.append(b['GXT'])
        
        elif gender == 'female':
            self.ftexturelist = self.fJsonObj[str(IDnum)]

            print("\nnumber of " + self.fdir + " textures: ", len(self.ftexturelist))
            for i in range(len(self.ftexturelist)):
                b = self.ftexturelist[str(i)]
                print(str(IDnum) + ' -', i, "=  Text Label: ", b["GXT"], "  In-store Name: " + b["Localized"])
                self.ftexturesfound.append(b['GXT'])
        
        elif gender == 'masks':
            self.mtexturelist = self.maskJsonObj[str(IDnum)]
            print("\nnumber of " + self.maskdir + " textures: ", len(self.maskJsonObj))
            for i in range(len(self.mtexturelist)):
                b = self.mtexturelist[str(i)]
                print(str(IDnum) + ' -', i, "=  Text Label: ", b["GXT"], "  In-store Name: " + b["Localized"])
                self.mtexturesfound.append(b['GXT'])