
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

dic = read_dic("dic_ec.txt")
#for name in dic:
#    print( name +" " + dic[name][0] + " " + dic[name][1])
#    pass

