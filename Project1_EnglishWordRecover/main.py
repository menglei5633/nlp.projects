import sys
import re

class RecoverWord:

    __dic = {}
    __buguizeVerbs = {}
    __buguizeNones = {}

    def recoverWord(self, test_word):  
        if test_word in self.__dic:
            print("词典中匹配到的：")
            print(test_word + ": " + self.__dic[test_word])
            #exit()
    
        if test_word in self.__buguizeVerbs:
            print("通过不规则动词还原：")
            word = self.__buguizeVerbs.get(test_word)
            print(word + ": " + self.__dic[word])
            return
        if test_word in self.__buguizeNones:
            print("通过不规则名词还原：")
            word = self.__buguizeNones.get(test_word)
            print(word + ": " + self.__dic[word])
            return
        
        word = self.__guize_change(test_word)
        if word:
            print("通过规则变换：")
            print(word + ": " + self.__dic[word])
            pass
        else:
            print("没有找到")
            pass
        return

    def __init__(self, dic_file, verb_file, none_file):
        self.__setDic(dic_file)
        self.__setBuguizeVerbs(verb_file)
        self.__setBuguizeNones(none_file)
        pass

    def __setDic(self, filename):
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
        self.__dic = dic

    def __setBuguizeVerbs(self, filename):
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
        self.__buguizeVerbs = buguizeVerb

    def __setBuguizeNones(self, filename):
        fileHandle = open(filename, "r")
        lineList = fileHandle.readlines()
        dic = {}
        for line in lineList:
            #print(line)
            line = line.replace("\n", "")
            wordList = line.split(" ")
            #print(wordList[1] + " " + wordList[0])
            dic[wordList[1]] = wordList[0]
            pass
        self.__buguizeNones = dic

    def __guize_change(self, test_word):
        tw = test_word
        if tw[-3:-1] + tw[-1] == "ves":
            tw = tw[0:-3] + "f"
            if tw in self.__dic:
                return tw
        elif tw[-3:-1] + tw[-1] == "ies":
            tw = tw[0:-3] + "y"
            if tw in self.__dic:
                return tw
        elif tw[-2] + tw[-1] == "es":
            tw = tw[0:-2]
            if tw in self.__dic:
                return tw
        elif tw[-1] == "s":
            tw = tw[0:-1]
            if tw in self.__dic:
                return tw
        elif tw[-3:-1] + tw[-1] == "ing" and tw[-4] == tw[-5]:
            tw = tw[0:-4]
            if tw in self.__dic:
                return tw
        elif tw[-4:-1] + tw[-1] == "ying":
            tw = tw[0:-4] + "ie"
            if tw in self.__dic:
                return tw
        elif tw[-3:-1] + tw[-1] == "ing":
            tw = tw[0:-3]
            if tw in self.__dic:
                return tw
            else:
                tw = tw[0:-3] + "e"
                if tw in self.__dic:
                    return tw
        elif tw[-2] + tw[-1] == "ed" and tw[-3] == tw[-4]:
            tw = tw[0:-3]
            if tw in self.__dic:
                return tw
        elif tw[-3:-1] + tw[-1] == "ied":
            tw = tw[0:-3] + "y"
            if tw in self.__dic:
                return tw
        elif tw[-2] + tw[-1] == "ed":
            tw = tw[0:-2]
            if tw in self.__dic:
                return tw
            else:
                tw = tw + "e"
                if tw in self.__dic:
                    return tw
        else:
            return None



dic_file = sys.argv[1]
buguizeV_file = sys.argv[2]
buguizeN_file = sys.argv[3]
test_word = sys.argv[4]

wordRecover = RecoverWord(dic_file, buguizeV_file, buguizeN_file)

wordRecover.recoverWord(test_word)

#dic = read_dic(dic_file)
#buguizeVerbs = read_BuguizeVerb(buguizeV_file)
#buguizeNones = read_BuguizeNone(buguizeN_file)




