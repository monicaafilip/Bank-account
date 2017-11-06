'''
Created on Nov 1, 2017

@author: Monica
'''
def checkZi(zi):
    if zi<1 or zi>31:
        return False
    else:
        return True

def checkSum(sum):
    if sum<0:
        return False
    else:
        return True

def checkTip(tip):
    if tip not in ["intrare","iesire"]:
        return False
    else:
        return True
    