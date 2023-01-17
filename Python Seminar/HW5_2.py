import itertools
from os import path


def RleStr(st):
    s = ""
    for i, o in itertools.groupby(st):
        q = list(o)
        s += str(len(q)) + i
    return s


def Coder():
    name1 = "text.txt"
    ifile = open(name1, "r", encoding="utf-8").read().splitlines()
    name2 = "text_code.txt"
    ofile = open(name2, "w+", encoding="utf-8")
    # ifile=file.read().splitlines()
    of = []
    for i in ifile:
        q = RleStr(i)
        # of.append(q)
        q += "\n"
        ofile.writelines(q)

    ofile.close()


def DeCoder():
    name1 = "text_code.txt"
    ifile = open(name1, "r", encoding="utf-8").read().splitlines()
    name2 = "text_Decode.txt"
    ofile = open(name2, "w+", encoding="utf-8")
    of = []
    for i in ifile:
        q = ""
        of=[]
        for ii in i:
            if ii.isdigit():
                q += ii
            else:
                of.append(ii * int(q))
                q = ""
        of.append("\n")
        ofile.writelines(of)

    ofile.close()


Coder()
DeCoder()
