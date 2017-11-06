'''
Created on Oct 24, 2017

@author: Monica
'''
from validare import validareTranzactie
from domeniu import *
from pydoc import sort_attributes

def adaugaTranzactie(lista,zi,suma,tip):
    '''
    functia adauga o tranzactie cu ziua:zi,suma:suma si tipul:tip date ca parametru
    date in:lista,zi,suma,tip
    date out:-
    '''
    tr=creeazaTranzactie(zi,suma,tip)
    validareTranzactie(tr)
    adauga(lista,tr)
    
def creeazaTranzactie(zi,suma,tip):
    '''
    date in:zi,suma,tip
    date out:tranzactia ce contine zi,suma,tip
    '''
    tr={}
    setZi(tr,zi)
    setSuma(tr,suma)
    setTip(tr,tip)
    return tr
           
def actualizareTranzactie(lista,tr,nouaSuma,noulTip):
    '''
    functia actualizeaza o tranzactie in care imi sunt date ziua,suma si tipul
    date in:lista,zi,suma,tip
    date out:-
    '''
    validareTranzactie(tr)
    for i in lista:
        if getZi(i)==getZi(tr) and getSuma(i)==getSuma(tr) and getTip(i)==getTip(tr):
            setSuma(i,nouaSuma)
            setTip(i,noulTip)
            
        
     
def stergeTranzactieZi(lista,zi):
    '''
    functia sterge tranzactia dintr-o zi citita de la tastatura
    date in:lista,zi
    date out: date out:variabila sters ce ia valoarea 1 daca s-au sters tranzactii
                                                      0 altfel
    '''
    sters=0
    i=0
    while i<len(lista):
        if getZi(lista[i])==zi:
            sterge(lista,i)
            sters=1
        i+=1
    return sters
   

def stergeTranzactiePerioada(lista,inceput,sfarsit):
    '''
    functia sterge tranzactia dintr-o perioada data
    date in:lista ziua de inceput:inceput si ziua de sfarsit:sfarsit
    date out: date out:variabila sters ce ia valoarea 1 daca s-au sters tranzactii
                                                      0 altfel
    '''
    sters=0
    i=0
    while i<len(lista):
        if getZi(lista[i])>=inceput and getZi(lista[i])<=sfarsit:
            sterge(lista, i)
            sters=1
            i-=1
        i+=1
    return sters


def stergeTranzactieTip(lista,tip):   
    '''
    functia sterge o tranzactie de un anumit tip
    date in:lista si tipul:tip
    date out: date out:variabila sters ce ia valoarea 1 daca s-au sters tranzactii
                                                        0 altfel
    '''
    sters=0
    i=0
    while i<len(lista):
        if getTip(lista[i])==tip:
            sterge(lista, i)
            sters=1
            i-=1
        i+=1
    return sters
   
def tiparesteTranzactiiSuma(lista,suma):
    '''
    functia tipareste tranzactiile cu suma mai mare decat o suma data
    date in:lista si suma:suma
    date out: date out:variabila tiparit ce ia valoarea 1 daca s-au tiparit tranzactii
                                                        0 altfel
    '''
    tiparit=0
    for i in lista:
        if getSuma(i)>suma:
            tiparesteTranzactie(i)
            tiparit=1
    return tiparit
    
def tiparesteTranzactiiZiSuma(lista,zi,suma):
    '''
    functia tipareste tranzactiile care au suma mai mare decat o suma data si au fost efectuate inainte de o zi data
    date in:lista,zi,suma
    date out: date out:variabila tiparit ce ia valoarea 1 daca s-au tiparit tranzactii
                                                        0 altfel
    '''
    tiparit=0
    for i in lista:
        if getZi(i)<zi and getSuma(i)>suma:
            tiparesteTranzactie(i)
            tiparit=1
    return tiparit
    
def tiparesteTranzactiiTip(lista,tip):
    '''
    functia tipareste tranzactiile de un anumit tip
    date in:lista
    date out:variabila tiparit ce ia valoarea 1 daca s-au tiparit tranzactii
                                              0 altfel
    '''
    tiparit=0
    for i in lista:
        if getTip(i)==tip:
            tiparesteTranzactie(i)
            tiparit=1
    return tiparit

def sumaTotalaTrAcelasiTip(lista,tip):
    '''
    functia calculeaza suma tranzactiilor de acelasi tip
    date in:lista si tipul
    date out:suma
    '''
    suma=0
    for i in lista:
        if getTip(i)==tip:
            suma+=getSuma(i)
    return suma

def verificareExistentaZi(lista,zi):
    '''
    functia verifica existenta unei tranzactii cu o zi data
    date in:lista si ziua 
    date out:1 daca exista tranzactii cu ziua data
             0 altfel
    '''
    i=0
    while i<len(lista):
        if getZi(lista[i])==zi:
            return 1
        i+=1
    return 0
        

def soldCont(lista,zi):
    '''
    functia calculeaza soldul contului dintr o zi data
    date in:lista si ziua
    date out:soldul 
    '''
    sold=0
    i=0
    if verificareExistentaZi(lista,zi):
        while i<len(lista):
            if getTip(lista[i])=='intrare' and getZi(lista[i])==zi:
                sold+=getSuma(lista[i])
            else:
                sold-=getSuma(lista[i])
            i+=1
    return sold

def tiparireTrAcelasiTipOrdonateSuma(lista,tip):
    '''
    functia tipareste tranzactiile de acelasi tip ordonate dupa suma
    date in:lista si tipul
    date out:-
    '''
    newL=[]
    for i in lista:
        if getTip(i)==tip:
            adaugaTranzactie(newL,getZi(i),getSuma(i),getTip(i))
    newL = sorted(newL, key=lambda k: getSuma(k))
    return newL
    
def eliminaTranzactiiSumaData(lista,suma):
    '''
    functia elimina tranzactiile cu o suma data
    date in:lista si suma 
    date out:variabila eliminat ce ia valoarea 1 sau 0 daca s-a eliminat vreo tranzactie sau nu
    '''
    eliminat=0
    i=0
    while i<len(lista):
        if getSuma(lista[i])==suma:
            sterge(lista,i)
            eliminat=1;
            i-=1
        i+=1
    return eliminat
            
def eliminaTranzactiiMaiMiciSuma(lista,suma,tip):
    '''
    functia elimina tranzactiile mai mici decat o suma data si cu acelasi tip
    date in:lista suma si tipul
    date out:variabila eliminat ce ia valoarea 1 sau 0 daca s-a eliminat vreo tranzactie sau nu
    '''
    eliminat=0
    i=0
    while i<len(lista):
        if getSuma(lista[i])<suma and getTip(lista[i])==tip:
            sterge(lista,i)
            eliminat=1;
            i-=1
        i+=1
    return eliminat

