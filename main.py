import os
from enum import StrEnum

class symbols(StrEnum):
    line = "│ "
    continues= "├"
    endline= "└"
    empty = "  "

previous = [False] * 100


def makePrefix(deep: int, endline: bool=False) -> str:
    result = ""

    if deep < 1:
        return result

    for i in range(deep-1):
        result += symbols.line if previous[i] else symbols.empty
    
    if endline:
        return result + symbols.endline

    return result + symbols.continues

def rec(path: str='.', name='.', deep: int=0, endline=False):
    if not os.path.exists(path):
        return 
    
    if os.path.isfile(path):
        print(makePrefix(deep, endline), name)
        return 

    arrDir = os.listdir(path)
    size = len(arrDir)

    previous[deep] = True 
    print(makePrefix(deep, endline) + name + '/')

    if deep > 0 and endline:
        previous[deep-1] = False

    for ind, obj in enumerate(sorted(arrDir), start=1):
        rec(path=path + '/' + obj, name=obj, deep=deep+1, endline=ind == size)
    
    previous[deep] = False




if __name__ == '__main__':
    print("The full current directory is: ", os.getcwd())
    rec('.')