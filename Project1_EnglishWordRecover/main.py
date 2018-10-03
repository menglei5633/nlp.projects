
def read_dic(filename):
    fileHandle = open(filename, "r")
    dic = {}
    lineList = fileHandle.readlines()
    for line in lineList:
        wordList = line.split(" ")
        for i in range(3, len(wordList)):
            wordList[2] = wordList[2] + wordList[i]
            pass
        #print("word: " + wordList[0] + "  %d\n" %  len(wordList))
        dic[wordList[0]] = [wordList[1], wordList[2]]
        pass
    return dic
    pass

def read_BuguizeVerb(filename):
    fileHandle = open(filename, "r")
    buguizeVerb = {}
    lineList = fileHandle.readlines()
    for line in lineList:
        #print(line)
        wordList = line.split(" ")
        guoqushiList = wordList[1].split(",")
        guoqufenciList = wordList[2].split(",")
        for word in guoqushiList:
            buguizeVerb[word] = wordList[0]
            pass
        for word in guoqufenciList:
            buguizeVerb[word] = wordList[0]
            pass
        pass
    return buguizeVerb
    pass

def read_buguizeNone(filename):
    fileHandle = open(filename, "r")
    lineList = fileHandle.readlines()
    dic = {}
    for line in lineList:
        #print(line)
        wordList = line.split(" ")
        '''
        for i in range(len(wordList)):
            print(wordList[i])
            pass
        print("______")
        '''
        dic[wordList[1]] = wordList[0]
        pass
    return dic
    pass

#dic = read_dic("dic_ec.txt")
#for name in dic:
#    print( name +" " + dic[name][0] + " " + dic[name][1])
#    pass
#buguizeVerb = read_BuguizeVerb("IrregularVerbList")
#for name in buguizeVerb:
#    print( "key: " + name + " value: " + buguizeVerb[name])
#    pass

buguizeNone = read_buguizeNone("IrregularPluralNouns")
for name in buguizeNone:
    print("key: " + name + " value: " + buguizeNone[name])
    pass


