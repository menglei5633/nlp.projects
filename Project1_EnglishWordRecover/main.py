import sys
import re

def read_dic(filename):
    fileHandle = open(filename, "r")
    dic = {}
    lineList = fileHandle.readlines()
    for line in lineList:
        wordList = line.split(" ")
        for i in range(2, len(wordList)):
            wordList[1] = wordList[1] + wordList[i]
            pass
        #print( wordList[0] + " " + wordList[1] + " " + wordList[2])
        dic[wordList[0]] = wordList[1]
        pass
    return dic
    pass

def read_BuguizeVerb(filename):
    fileHandle = open(filename, "r")
    buguizeVerb = {}
    lineList = fileHandle.readlines()
    for line in lineList:
        #print(line)
        line = line.replace("\n", "")
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

def read_BuguizeNone(filename):
    fileHandle = open(filename, "r")
    lineList = fileHandle.readlines()
    dic = {}
    for line in lineList:
        #print(line)
        line = line.replace("\n", "")
        wordList = line.split(" ")
        '''
        for i in range(len(wordList)):
            print(wordList[i])
            pass
        print("______")
        '''
        #print(wordList[1] + " " + wordList[0])
        dic[wordList[1]] = wordList[0]
        pass
    return dic


def other_fuc(test_word, dic):
    guizes = [["ves$","f"],["ies$","y"], ["es$",""], ["s$",""], ["([a-zA-Z])$1{2}ing$","?"],
            ["ying$","ie"], ["ing$",""], ["ing$","e"], ["([a-zA-Z])$1{2}ed$","?"], ["ied$","y"],
            ["ed$",""], ["ed$","e"]]
    word = ""
    for i in range(len(guizes)):
        pattern = guizes[i][0]
        replace = guizes[i][1]
        print(pattern)
        if replace != "?":
            word = re.sub(pattern, replace, test_word)
            print("word: " + word)
            if word in dic:
                return word
            pass
        else:
            match_str = re.search(pattern, test_word, re.I)
            if match_str:
                print("match: " + match_str.group())
                first = match_str.group()[0:1]
                word = re.sub(pattern, first, test_word)
                if word in dic:
                    return word
                pass
            pass
        pass
    return None

#dic = read_dic("dic_ec.txt")
#for name in dic:
#    print( name +" " + dic[name][0] + " " + dic[name][1])
#    pass
#buguizeVerb = read_BuguizeVerb("IrregularVerbList")
#for name in buguizeVerb:
#    print( "key: " + name + " value: " + buguizeVerb[name])
#    pass
'''
buguizeNone = read_buguizeNone("IrregularPluralNouns")
for name in buguizeNone:
    print("key: " + name + " value: " + buguizeNone[name])
    pass
'''
dic_file = sys.argv[1]
buguizeV_file = sys.argv[2]
buguizeN_file = sys.argv[3]
test_word = sys.argv[4]

dic = read_dic(dic_file)
buguizeVerbs = read_BuguizeVerb(buguizeV_file)
buguizeNones = read_BuguizeNone(buguizeN_file)

if test_word in dic:
    print(test_word + ": " + dic[test_word])
    exit()

if test_word in buguizeVerbs:
    word = buguizeverbs.get(test_word)
    print(word + ": " + dic[word])
    exit()
if test_word in buguizeNones:
    word = buguizeNones.get(test_word)
    print(word + ": " + dic[word])
    exit()
print("other")
word = other_fuc(test_word, dic)
if word:
    print(word + ": " + dic[word])
    pass
else:
    print("not find")
    pass
exit()

