'''
Created on Nov 5, 2017

@author: Monica
'''
import uiInt
import uiText
from domeniu import *

def mainBoth():
    print("Meniu Cont Bancar:")
    optiuni={1:[uiInt.comenziInt,"1.Comenzi intregi"],2:[uiText.comenziText,"2.Comenzi text"]}
    info={"lista":[],"undo":[],"phrase":""}
    menu(optiuni,info)

def menu(optiuni,info):
    keep=getUndo(info)
    lista=getLista(info)
    while True:
        uiInt.afiseazaMeniu(optiuni)
        cmd=citesteInt("Introduceti comanda:")
        if cmd==0:
            undo=adaugaListaUndo(info)
            return
        if cmd in optiuni :
            undo=adaugaListaUndo(info)
            keep=getUndo(info)
            if cmd!=-1:
                try:
                    optiuni[cmd][0](info)
                except ValueError as ve:
                    print(ve)
            else:    
                if len(keep)>1:
                    info=uiInt.undo(info)
                    print("Undo efectuat cu succes!\n")
                elif len(keep)>0 and keep[0]!=[] and keep!=[]:
                    lista.clear()
                    keep.clear()
                    setLista(info,lista)
                    setUndo(info,keep)
                    print("Undo efectuat cu succes!\n")
                else:
                    print("Nu se mai poate efectua operatia de undo!\n")
        else:
            print("Comanda invalida!\n")
       
