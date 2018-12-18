import sys
import re

class MM:
    __dic = []
    __guize = {}
    __guize_before = {}
    __max_length = 0

    def __init__(self, dic_file, guize_file, guize_file1, max_length):
        self.__readDic(dic_file)
        self.__readGuize(guize_file)
        self.__readGuizeBefore(guize_file1)
        self.__max_length = max_length
    
    
    def fenci_fun(self, word_list):
        wl = word_list
        fenci = []
        if len(wl) == 0:
            return fenci
        #before
        for i in self.__guize_before:
            if wl.find(i) >= 0:
                wl_l = wl.split(i)[0]
                wl_r = wl.split(i)[1]
                fenci_ = self.fenci_fun(wl_l)
                for j in range(len(fenci_)):
                    fenci.append(fenci_[j])
                for j in range(len(self.__guize_before[i])):
                    fenci.append(self.__guize_before[i][j])
                fenci_ = self.fenci_fun(wl_r)
                for j in range(len(fenci_)):
                    fenci.append(fenci_[j])
                return fenci
        #fmm and rmm
        fenci1 = self.fmm(wl)
        fenci2 = self.rmm(wl)[::-1]
        
        
        #存在歧义
        if fenci1 != fenci2:
            #print("歧义")
            for i in self.__guize:
                index = wl.find(i)
                if index >= 0:
                    wl_l = wl.split(i)[0]
                    wl_r = wl.split(i)[1]
                    fenci_ = self.fenci_fun(wl_l)
                    for j in range(len(fenci_)):
                        fenci.append(fenci_[j])
                    for j in range(len(self.__guize[i])):
                        fenci.append(self.__guize[i][j])
                    fenci_ = self.fenci_fun(wl_r)
                    for j in range(len(fenci_)):
                        fenci.append(fenci_[j])
                    break
            if fenci == []:
                fenci = [fenci1, fenci2]
        else:
            fenci = fenci2
        return fenci 
    
    def fmm(self, word_list):
        s = 0
        wl = word_list
        fenci = []
        while s < len(wl):
            word_ = ""
            i_ = -1
            #print(s)
            if s == len(wl) - 1:
                fenci.append(wl[-1])
                break
            for i in range(self.__max_length, 0, -1):
                word = wl[s:s+i]
                #print(word)
                if i == 1:
                    i_ = i
                    fenci.append(word)
                    break
                if word in self.__dic and i > i_:
                    #print("ok")
                    fenci.append(word)
                    i_ = i
                    break
            s = s + i_
        return fenci
    
    def rmm(self, word_list):
        wl = word_list
        s = len(wl)
        fenci = []
        while s > 0:
            word_ = ""
            i_ = len(wl) + 1
            #print(s)
            if s == 1:
                fenci.append(wl[0])
                break
            for i in range(self.__max_length, 0, -1):               
                if s - i < 0:
                    i = s - 0
                word = wl[s - i: s]
                #print(word)
                if word in self.__dic:
                    #print("ok break")
                    fenci.append(word)
                    break
            #print(i)
            s = s - i
            #print(s)
        
        return fenci

    def __readDic(self, filename):
        fileHandle = open(filename, "r")
        dic = []
        lineList = fileHandle.readlines()
        for line in lineList:
            line = line.split("\n")[0]
            line = line.split(",")[0]
            if line == "":
                continue
            dic.append(line)
            pass
        self.__dic = dic

    def __readGuize(self, filename):
        fileHandle = open(filename, "r")
        guize = {}
        lineList = fileHandle.readlines()
        for line in lineList:
            line = line.split("\n")[0]
            qiyi = line.split(" ")[0]
            fenci = line.split(" ")[1].split("/")
            if qiyi == "":
                continue
            guize[qiyi] = fenci
            pass
        self.__guize = guize

    def __readGuizeBefore(self, filename):
        fileHandle = open(filename, "r")
        guize = {}
        lineList = fileHandle.readlines()
        for line in lineList:
            line = line.split("\n")[0]
            qiyi = line.split(" ")[0]
            fenci = line.split(" ")[1].split("/")
            if qiyi == "":
                continue
            guize[qiyi] = fenci
            pass
        self.__guize_before = guize

    def printDic(self):
        for i in range(len(self.__dic)):
            print(self.__dic[i])

            

pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
dic_file = sys.argv[1]
guize_file = sys.argv[2]
guize_file1 = sys.argv[3]
max_length = int(sys.argv[4])
text = sys.argv[5]

#根据标点符号分割句子
text_list = re.split(pattern, text)

mm = MM(dic_file, guize_file, guize_file1, max_length)
#mm.printDic()
for i in range(len(text_list)):
    print(mm.fenci_fun(text_list[i]))
    
    

