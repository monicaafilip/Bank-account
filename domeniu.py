'''
Created on Oct 24, 2017

@author: Monica
'''
import copy
def citesteInt(text):
    while True:
        try:
            x=int(input(text))
            return x
        except ValueError:
            print("Invalid!Valorea trebuie sa fie de tip int")


def citesteFloat(text):
    while True:
        try:
            x=float(input(text))
            return x
        except ValueError:
            print("Invalid!Valoarea trebuie sa fie de tip float")

def citesteTip(text):
    while True:
        try:
            x=input(text)
            return x
        except ValueError():
                print("Invalid! Tipul trebuie sa fie de intrare sau iesire")
   
def verifErori(erori):
    '''
    functia verifica daca am gasit erori,in caz afirmativ afisandu-i-le userului
    date in:erori
    date out:-
    '''
    if len(erori)>0:
        raise ValueError(erori)
     
def adauga(lista,x):
    '''
    functia adauga un element in lista
    date in:lista si elementul x
    date out:-
    '''
    lista.append(x)
    
def adaugaLista(lista,listaElement):
    '''
    functia adauga intr-o lista ca un nou element o noua lista
    date in:lista si lista ce av fi noul element
    date out:-
    '''
    lista.append(list(listaElement))
    
def sterge(lista,x):
    '''
    functia sterge elementul x din lista
    date in:lista si elementul x
    date out:-
    '''
    del lista[x]
    
def tiparesteTranzactie(tr):
    '''
    functia tipareste o tranzactie data ca parametru
    date in:tranzactia data
    date out:-
    '''
    print("Tranzactia cu ziua:",getZi(tr),",suma:",getSuma(tr),"si tipul:",getTip(tr))

def adaugaListaUndo(info):
    keep=getUndo(info)
    lista=getLista(info)
    if(len(keep)!=0 and keep[-1]!=lista)or len(keep)==0:
                copie=copy.deepcopy(lista)
                adaugaLista(keep,copie)
                setUndo(info,keep)
    return getUndo(info)

def afisareTranzactii(lista):
    i=0
    while i<len(lista):
        tiparesteTranzactie(lista[i])
        i+=1
        
def verificareExistenta(lista,zi):
    i=0
    while i<len(lista):
        if getZi(lista[i])==zi:
            return 1
        i+=1
    return 0

def getZi(tr):
    return tr["zi"]
    
def setZi(tr,zi):
    tr["zi"]=zi

def getSuma(tr):
    return tr["suma"]

def setSuma(tr,suma):
    tr["suma"]=suma

def getTip(tr):
    return tr["tip"]

def setTip(tr,tip):
    tr["tip"]=tip

def getLista(lista):
    return lista["lista"]

def setLista(lista,newL):
    lista["lista"]=copy.deepcopy(newL)
    
def getUndo(lista):
    return lista["undo"]

def setUndo(lista,newL):
    lista["undo"]=copy.deepcopy(newL)
    
def getPhrase(lista):
    return lista["phrase"]

def setPhrase(lista,phrase):
    lista["phrase"]=phrase
    
def setInfo(info,newInfo):
    setLista(info,getLista(newInfo))
    setUndo(info,getUndo(newInfo))
    setPhrase(info,getPhrase(newInfo))
    