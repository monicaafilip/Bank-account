'''
Created on Oct 24, 2017

@author: Monica
'''
import menus
from functionalitati import *
from domeniu import *
from validare import *
import copy

def comenziInt(info):
    optiuniP={1:[adaugare,"1.Adaugare"],2:[stergere,"2.Stergere"],3:[cautari,"3.Cautari"],4:[rapoarte,"4.Rapoarte"],5:[filtrare,"5.Filtrare"],6:[ui_afisareLista,"6.Afisare lista"],-1:[undo,"-1.UNDO"]}
    menus.menu(optiuniP,info)
    
def afiseazaMeniu(optiuni):
    print("Meniu:")
    for optiune in optiuni:
        print(optiuni[optiune][1])
    print("0.EXIT")

def adaugare(info):
    optiuni={1:[ui_adaugaTranzactie,"1.Adaugare tranzactie"],2:[ui_actualizareTranzactie,"2.Actualizare tranzactie"]}
    menus.menu(optiuni,info)
    
def stergere(info):
    optiuni={1:[ui_stergeTranzactieZi,"1.Sterge tranzactia dintr-o zi data"],2:[ui_stergeTranzactiePerioada,"2.Sterge tranzactie dintr-o perioada"],3:[ui_stergeTranzactieTip,"3.Sterge tranzactie de un tip"]}
    menus.menu(optiuni,info)
         
def cautari(info):
    optiuni={1:[ui_tiparesteTranzactiiSuma,"1.Tipareste o tranzactie mai mare decat o suma"],2:[ui_tiparesteTranzactiiZiSuma,"2.Tipareste tranzactii dinaintea unei zile si avand suma mai mare ca o suma data"],3:[ui_tiparesteTranzactiiTip,"3.Tipareste tranzactie de un anumit tip"]}   
    menus.menu(optiuni,info)
    
def rapoarte(info):
    optiuni={1:[ui_sumaTotalaTrAcelasiTip,"1.Suma totala a tranzactiilor de un anumit tip"],2:[ui_soldCont,"2.Soldul contului la o anumita data"],3:[ui_tiparireTrAcelasiTipOrdonateSuma,"3.Tiparire tranzactii de un anumit tip ordonate dupa suma"]}
    menus.menu(optiuni,info)

def filtrare(info):
    optiuni={1:[ui_eliminaTranzactiiSumaData,"1.Elimina tranzactiile cu o suma data"],2:[ui_eliminaTranzactiiMaiMiciSuma,"2.Elimina tranzactiile cu suma mai mica decat o suma data si cu acelasi tip"]}
    menus.menu(optiuni,info)
    
def undo(info):
    keep=getUndo(info)
    keep=keep[:-1]
    setLista(info,keep[-1])
    setUndo(info,keep)
    return info

def ui_adaugaTranzactie(info):
    '''
    functia adauga o noua tranzactie la finalul listei,in lista data ca parametru
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    zi=citesteInt("Dati ziua:")
    suma=citesteFloat("Dati suma:")
    tip=citesteTip("Dati tipul:")
    adaugaTranzactie(lista,zi,suma,tip)
    setLista(info,lista)
    print("Tranzactie adaugata cu succes!\n")

def ui_actualizareTranzactie(info):
    '''
    functia actualizeaza o tranzactie in care imi sunt date ziua,suma si tipul
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    zi=citesteInt("Dati ziua:")
    suma=citesteFloat("Dati suma:")
    tip=citesteTip("Dati tipul:")
    tr={}
    setZi(tr,zi)
    setSuma(tr,suma)
    setTip(tr,tip)
    validareTranzactie(tr)
    nouaSuma=citesteFloat("Dati noua suma:")
    validareSuma(nouaSuma, erori)
    noulTip=citesteTip("Dati noul tip:")
    validareTip(noulTip,erori)
    if tr in lista:
        actualizareTranzactie(lista,tr,nouaSuma,noulTip)
        setLista(info,lista)
        print("Tranzactie actualizata cu succes!\n") 
    else:
        print("Tranzactia nu se afla in baza noastra de date.Actualizati o zi care exista sau eventual adaugati o alta tranzactie!\n")
     
def ui_stergeTranzactieZi(info):
    '''
    functia sterge tranzactia dintr-o zi citita de la tastatura
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    ziua=citesteInt("Dati ziua:")
    validareZi(ziua,erori)
    sters=stergeTranzactieZi(lista,ziua)
    if sters==0:
        print("Ziua data nu se afla in baza de date!Introduceti una valida sau alegeti alta comanda!\n")
    else:
        setLista(info,lista)        
        setUndo(info,adaugaListaUndo(info))
        print("Tranzactie stearsa cu succes!\n")
       
def ui_stergeTranzactiePerioada(info):
    '''
    functia sterge tranzactia dintr-o zi perioada data
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    ziInceput=citesteInt("Dati ziua de inceput:")
    validareZi(ziInceput,erori)
    ziSfarsit=citesteInt("Dati ziua de sfarsit:")
    validareZi(ziSfarsit, erori)
    if ziInceput<ziSfarsit:
        sters=stergeTranzactiePerioada(lista,ziInceput,ziSfarsit)
        if sters==1:
            setLista(info,lista)
            info=adaugaListaUndo(info)
            print("Tranzactii sterse cu succes!\n")
        else:
            print("Nu s-au gasit tranzactii in perioada data!")
    else:
        print("Perioada invalida!Adaugati una valida sau introduceti alta comanda!\n")

def ui_stergeTranzactieTip(info):
    '''
    functia sterge o tranzactie de un anumit tip
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    tip=citesteTip("Dati tipul:")
    validareTip(tip, erori)
    sters=stergeTranzactieTip(lista,tip)
    if sters==0:
        print("Tipul dat nu a fost adaugat in baza de date!Adaugati alt tip sau introduceti alta comanda!\n")
    else:
        print("Tranzactii sterse cu succes!\n")
        setLista(info,lista)
        info=adaugaListaUndo(info)

def ui_tiparesteTranzactiiSuma(info):
    '''
    functia tipareste tranzactiile cu suma mai mare decat o suma data
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    suma=citesteFloat("Dati suma:")
    validareSuma(suma,erori)
    tiparit=tiparesteTranzactiiSuma(lista,suma)
    if tiparit==0:
        print("Nu au fost gasite tranzactii mai mari decat suma data.Dati alta suma sau alegeti alta comanda!\n")
    else:
        print("Tiparire efectuata cu succes!\n")
        
def ui_tiparesteTranzactiiZiSuma(info):
    '''
    functia tipareste tranzactiile care au suma mai mare decat o suma data si au fost efectuate inainte de o zi data
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    zi=citesteInt("Dati ziua:")
    validareZi(zi,erori)
    suma=citesteFloat("Dati suma:")
    validareSuma(suma,erori)
    tiparit=tiparesteTranzactiiZiSuma(lista,zi,suma)
    if tiparit==0:
        print("Nu au fost gasite tranzactii efectuate inainte de ziua data si mai mari ca suma. Adaugati alte valori sau alegeti alta comanda!\n")
    else:
        print("Tiparire efectuata cu succes!\n")
   
def ui_tiparesteTranzactiiTip(info):
    '''
    functia tipareste tranzactiile de un anumit tip
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    tip=citesteTip("Dati tipul:")
    validareTip(tip,erori)
    tiparit=tiparesteTranzactiiTip(lista,tip)
    if tiparit==0:
        print("Nu au fost gasite tranzactii efectuate de tipul dat. Dati alt tip sau alegeti alta comanda!\n")
    else:
        print("Tiparire efectuata cu succes!\n")

def ui_sumaTotalaTrAcelasiTip(info):
    '''
    functia calculeaza suma tranzactiilor de acelasi tip
    date in:lista
    date out:-
    '''
    erori=""
    lista=getLista(info)
    tip=citesteTip("Dati tipul:")
    validareTip(tip,erori)
    s=sumaTotalaTrAcelasiTip(lista,tip)
    if s<=0:
        print("Nu s-au gasit tranzactii pentru tipul introdus.Introduceti alt tip sau alegeti alta comanda!\n")
    else:
        print("Suma este ",s,".\n")

def ui_soldCont(info):
    '''
    functia calculeaza soldul contului la o zi data de utilizator
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    zi=citesteInt("Dati ziua:")
    validareZi(zi, erori)
    sold=soldCont(lista,zi)
    exista=verificareExistenta(lista,zi)
    if exista==1 :
        print("Raport efectuat cu succes.Soldul contului pentru ziua data este",sold,".\n")
    else:
        print("Data nu a fost introdusa in baza de date.Actualizati baza de date sau alegeti alta comanda!\n")
        
def ui_tiparireTrAcelasiTipOrdonateSuma(info):
    '''
    functia tipareste tranzactiile de acelasi tip ordonate crescator dupa suma
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    newL=[]
    tip=citesteTip("Dati tipul:")
    validareTip(tip,erori)
    newL=tiparireTrAcelasiTipOrdonateSuma(lista,tip)
    if len(newL)==0:
        print("Nu s-au gasit tranzactii de tipul dat. Actualizati baza de date sau alegeti alta comanda!\n")
    else:
        afisareTranzactii(newL)

def ui_eliminaTranzactiiSumaData(info):
    '''
    functia elimina tranzactiile ce au o anumita suma
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    erori=""
    suma=citesteFloat("Dati suma:")
    validareSuma(suma, erori)
    eliminat=eliminaTranzactiiSumaData(lista,suma)
    if eliminat==0:
        print("Nu s-au gasit tranzactii cu suma data. Actualizati baza de date sau aleegti alta comanda!\n")
    else:
        print("Eliminare efectuata cu succes!\n")
        setLista(info,lista)
        
    
def ui_eliminaTranzactiiMaiMiciSuma(info):
    '''
    functia elimina tranzactiile mai mici decat o suma data si cu acelasi tip
    date in:lista
    dat out:-
    '''
    lista=getLista(info)
    erori=""
    suma=citesteFloat("Dati suma:")
    validareSuma(suma, erori)
    tip=citesteTip("Dati tipul:")
    validareTip(tip, erori)
    eliminat=eliminaTranzactiiMaiMiciSuma(lista,suma,tip)
    if eliminat==0:
        print("Nu s-au gasit tranzactii mai mici ca suma data si cu tipul dat.Actualizati baza de date sau alegeti alta comanda!\n")
    else:
        print("Eliminare efectuata cu succes!\n")
        setLista(info,lista)
        
def ui_afisareLista(info):
    '''
    functia afiseaza lista data ca parametru
    date in:lista
    date out:-
    '''
    lista=getLista(info)
    i=0
    while i<len(lista):
        tiparesteTranzactie(lista[i])
        i+=1
    if len(lista)==0:
        print(lista)
    
