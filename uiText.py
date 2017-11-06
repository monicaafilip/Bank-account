
'''
Created on Nov 5, 2017
@author: Monica
'''
from domeniu import *
from functionalitati import *
from validare import *
import uiInt
def comenziText(info):
    optiuniP={1:[adaugareTxt,"Adaugare('add')"],2:[stergereTxt,"Stergere('del')"],3:[cautariTxt,"Cautari('find')"],4:[rapoarteTxt,"Rapoarte('rap')"],5:[filtrareTxt,"Filtrare('fil')"],6:[uiInt.ui_afisareLista,"Afisare lista(printL)"],-1:[uiInt.undo,"Undo(undo)"]}
    menuTxt(optiuniP,info)
    
def menuTxt(optiuni,info):
    keep=getUndo(info)
    lista=getLista(info)
    while True:
        afiseazaMeniuTxt(optiuni)
        cmd=input("Introduceti comanda:")
        if cmd=='exit':
            #info=adaugaListaUndo(info)
            return
        if cmd=='add':
            optiuni[1][0](info)
            setUndo(info,adaugaListaUndo(info))
        elif cmd=='del':
            optiuni[2][0](info)
            setUndo(info,adaugaListaUndo(info))
        elif cmd=='find':
            optiuni[3][0](info)
        elif cmd=='rap':
            optiuni[4][0](info)
        elif cmd=='fil':
            optiuni[5][0](info)
            setUndo(info,adaugaListaUndo(info))
        elif cmd=="printL":
            optiuni[6][0](info)
        elif cmd=="undo":
            if len(keep)>1:
                info=uiInt.undo(info)
                print("Undo efectuat cu succes!\n")
            elif len(keep)>0 and keep[0]!=[]:
                lista.clear()
                keep.clear()
                print("Undo efectuat cu succes!\n")
            else:
                print("Nu se mai poate efectua operatia de undo\n")
        else:
            print("Comanda invalida!\n")
        
            
def menuT(optiuni,info):
    
    while True:
        afiseazaMeniuTxt(optiuni)
        phrase=input("Introduceti comanda:")
        phrase=phrase.split(" ")
        setPhrase(info,phrase)
        try:
            if phrase[0]=="exit"  :
                return
            elif (phrase[0]=="add" and len(phrase)==4) or (phrase[0]=="deleteZ" and len(phrase)==2) or (phrase[0]=="printS" and len(phrase)==2) or (phrase[0]=="sumT" and len(phrase)==2) or (phrase[0]=="remove" and len(phrase)==2) :
                optiuni[1][0](info)
            elif (phrase[0]=="update" and len(phrase)==6)or  (phrase[0]=="delete" and len(phrase)==3) or  (phrase[0]=="print" and len(phrase)==3)or (phrase[0]=="sold" and len(phrase)==2) or (phrase[0]=="remove" and len(phrase)==3) :
                optiuni[2][0](info)
            elif (phrase[0]=="deleteT" and len(phrase)==2) or(phrase[0]=="printT" and len(phrase)==2) or (phrase[0]=="printST" and len(phrase)==2):
                optiuni[3][0](info)
            else:
                print("comanda invalida\n")
        except ValueError as ve:
                print(ve)
              
def afiseazaMeniuTxt(optiuni):
    print("Meniu:")
    for optiune in optiuni:
        print(optiuni[optiune][1])
    print("Exit('exit')\n")

def adaugareTxt(info):
    optiuni={1:[ui_adaugaTranzactieTxt,"Adaugare tranzactie('add' ziua suma tipul):"],2:[ui_actualizareTranzactieTxt,"Actualizare tranzactie('update' ziua suma tipul nouaSuma noulTip):"]}
    menuT(optiuni,info)

def stergereTxt(info):
    optiuni={1:[ui_stergeTranzactieZiTxt,"Sterge tranzactie('deleteZ' ziua): "],2:[ui_stergeTranzactiePerioadaTxt,"Sterge tranzactie dintr-o perioada('delete' inceput sfarsit):"],3:[ui_stergeTranzactieTipTxt,"Sterge tranzactie de un tip('deleteT' tipul):"]}
    menuT(optiuni,info)
         
def cautariTxt(info):
    optiuni={1:[ui_tiparesteTranzactiiSumaTxt,"Tipareste tranzactie mai mare decat o suma('printS' suma ):"],2:[ui_tiparesteTranzactiiZiSumaTxt,"Tipareste tranzactii dinaintea unei zile si avand suma mai mare ca o suma data('print' ziua suma"],3:[ui_tiparesteTranzactiiTipTxt,"Tipareste tranzactie de un anumit tip('printT' tip):"]}   
    menuT(optiuni,info)
    
def rapoarteTxt(info):
    optiuni={1:[ui_sumaTotalaTrAcelasiTipTxt,"Suma totala a tranzactiilor de un anumit tip('sumT' tip)"],2:[ui_soldContTxt,"Soldul contului la o anumita data('sold' zi):"],3:[ui_tiparireTrAcelasiTipOrdonateSumaTxt,"Tiparire tranzactii de un anumit tip ordonate dupa suma('printST' tip):"]}
    menuT(optiuni,info)

def filtrareTxt(info):
    optiuni={1:[ui_eliminaTranzactiiSumaDataTxt,"Elimina tranzactiile cu o suma data('remove' suma):"],2:[ui_eliminaTranzactiiMaiMiciSumaTxt,"Elimina tranzactiile cu suma mai mica decat o suma data si cu acelasi tip('remove' suma tip):"]}
    menuT(optiuni,info)
   
def ui_adaugaTranzactieTxt(info):
    '''
    functia adauga o noua tranzactie la finalul listei,in lista data ca parametru
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    zi=validareZiTxt(phrase[1])
    suma=validareSumaTxt(phrase[2])
    tip=phrase[3]
    validareTip(tip, erori)
    adaugaTranzactie(lista,zi,suma,tip)
    print("Tranzactie adaugata cu succes!\n")

def ui_actualizareTranzactieTxt(info):
    '''
    functia actualizeaza o tranzactie in care imi sunt date ziua,suma si tipul
   date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    zi=validareZiTxt(phrase[1])
    suma=validareSumaTxt(phrase[2])
    tip=phrase[3]
    validareTip(tip, erori)
    tr={}
    setZi(tr,zi)
    setSuma(tr,suma)
    setTip(tr,tip)
    validareTranzactie(tr)
    sumaNoua=validareSumaTxt(phrase[4])
    tipNou=phrase[5]
    validareTip(tipNou, erori)
    if tr in lista:
        actualizareTranzactie(lista,tr,sumaNoua,tipNou)
        print("Tranzactie actualizata cu succes!\n") 
    else:
        print("Tranzactia nu se afla in baza noastra de date.Actualizati o zi care exista sau eventual adaugati o alta tranzactie!\n")
     


def ui_stergeTranzactieZiTxt(info):
    '''
    functia sterge tranzactia dintr-o zi citita de la tastatura
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-'''
    erori=""
    lista=getLista(info)
    phrase=getPhrase(info)
    ziua=validareZiTxt(phrase[1])
    sters=stergeTranzactieZi(lista,ziua)
    if sters==0:
        print("Ziua data nu se afla in baza de date!Introduceti una valida sau alegeti alta comanda!\n")
    else:
        print("Tranzactie stearsa cu succes!\n")
       
def ui_stergeTranzactiePerioadaTxt(info):
    '''
    functia sterge tranzactia dintr-o zi perioada data
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    ziInceput=validareZiTxt(phrase[1])
    ziSfarsit=validareZiTxt(phrase[2])
    if ziInceput<ziSfarsit:
        sters=stergeTranzactiePerioada(lista,ziInceput,ziSfarsit)
        print("Tranzactii sterse cu succes!\n")
    else:
        print("Perioada invalida!Adaugati una valida sau introduceti alta comanda!\n")

def ui_stergeTranzactieTipTxt(info):
    '''
    functia sterge o tranzactie de un anumit tip
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    tip=phrase[1]
    validareTip(tip, erori)
    sters=stergeTranzactieTip(lista,tip)
    if sters==0:
        print("Tipul dat nu a fost adaugat in baza de date!Adaugati alt tip sau introduceti alta comanda!\n")
    else:
        print("Tranzactii sterse cu succes!\n")

def ui_tiparesteTranzactiiSumaTxt(info):
    '''
    functia tipareste tranzactiile cu suma mai mare decat o suma data
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    suma=validareSumaTxt(phrase[1])
    tiparit=tiparesteTranzactiiSuma(lista,suma)
    if tiparit==0:
        print("Nu au fost gasite tranzactii mai mari decat suma data.Dati alta suma sau alegeti alta comanda!\n")
    else:
        print("Tiparire efectuata cu succes!\n")
        
def ui_tiparesteTranzactiiZiSumaTxt(info):
    '''
    functia tipareste tranzactiile care au suma mai mare decat o suma data si au fost efectuate inainte de o zi data
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    zi=validareZiTxt(phrase[1])
    suma=validareSumaTxt(phrase[2])
    tiparit=tiparesteTranzactiiZiSuma(lista,zi,suma)
    if tiparit==0:
        print("Nu au fost gasite tranzactii efectuate inainte de ziua data si mai mari ca suma. Adaugati alte valori sau alegeti alta comanda!\n")
    else:
        print("Tiparire efectuata cu succes!\n")
   
def ui_tiparesteTranzactiiTipTxt(info):
    '''
    functia tipareste tranzactiile de un anumit tip
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    tip=phrase[1]
    validareTip(tip,erori)
    tiparit=tiparesteTranzactiiTip(lista,tip)
    if tiparit==0:
        print("Nu au fost gasite tranzactii efectuate de tipul dat. Dati alt tip sau alegeti alta comanda!\n")
    else:
        print("Tiparire efectuata cu succes!\n")

def ui_sumaTotalaTrAcelasiTipTxt(info):
    '''
    functia calculeaza suma totala a tranzactiilor de acelasi tip
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    erori=""
    lista=getLista(info)
    phrase=getPhrase(info)
    tip=phrase[1]
    validareTip(tip,erori)
    s=sumaTotalaTrAcelasiTip(lista,tip)
    if s<=0:
        print("Nu s-au gasit tranzactii pentru tipul introdus.Introduceti alt tip sau alegeti alta comanda!\n")
    else:
        print("Tiparire efectuata cu succes.Suma este ",s,".\n")

def ui_soldContTxt(info):
    '''
    functia calculeaza soldul tranzactiei dintr-o anumita zi
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    zi=validareZiTxt(phrase[1])
    sold=soldCont(lista,zi)
    exista=verificareExistenta(lista,zi)
    if exista==1 :
        print("Raport efectuat cu succes.Soldul contului pentru ziua data este",sold,".\n")
    else:
        print("Data nu a fost introdusa in baza de date.Actualizati baza de date sau alegeti alta comanda!\n")
        
def ui_tiparireTrAcelasiTipOrdonateSumaTxt(info):
    '''
    functia tipareste tranzactiile de acelasi tip ordonate crescator dupa suma
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    newL=[]
    tip=phrase[1]
    validareTip(tip,erori)
    newL=tiparireTrAcelasiTipOrdonateSuma(lista,tip)
    if len(newL)==0:
        print("Nu s-au gasit tranzactii de tipul dat. Actualizati baza de date sau alegeti alta comanda\n")
    else:
        afisareTranzactii(newL)

def ui_eliminaTranzactiiSumaDataTxt(info):
    '''
    functia elimina trazactiile ce au o suma data
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    suma=validareSumaTxt(phrase[1])
    eliminat=eliminaTranzactiiSumaData(lista,suma)
    if eliminat==0:
        print("Nu s-au gasit tranzactii cu suma data. Actualizati baza de date sau alegti alta comanda.\n")
    else:
        print("Eliminare efectuata cu succes!\n")
        
    
def ui_eliminaTranzactiiMaiMiciSumaTxt(info):
    '''
    functia elimina tranzactiile mai mici decat o suma 
    date in:lista si comenzile date ca stringuri(phrase)
    dat out:-
    '''
    lista=getLista(info)
    phrase=getPhrase(info)
    erori=""
    suma=validareSumaTxt(phrase[1])
    tip=phrase[2]
    validareTip(tip, erori)
    eliminat=eliminaTranzactiiMaiMiciSuma(lista,suma,tip)
    if eliminat==0:
        print("Nu s-au gasit tranzactii mai mici ca suma data si cu tipul dat.Actualizati baza de date sau alegeti alta comanda!\n")
    else:
        print("Eliminare efectuata cu succes!\n")            

