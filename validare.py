'''
Created on Oct 24, 2017

@author: Monica
'''
from domeniu import *
from util import *
def validareTranzactie(tranzactie):
    '''
    functia valideaza tranzactia si retine in erori eventualele erori,in cazul in care aceasta nu ar fi valida
    date in:tranzactie
    date out:-
    '''
    erori=""
    validareZi(getZi(tranzactie),erori)
    validareSuma(getSuma(tranzactie),erori)
    validareTip(getTip(tranzactie),erori)
   
def validareZi(zi,erori):
    '''
    functia valideaza ziua ca fiind o zi dintr-o luna cu 31 zile
    date in:zi,erori
    date out:-
    '''
    if checkZi(zi)==False:
        erori+="Zi invalida! nu este intre 1 si 31\n"
    verifErori(erori)
    
def validareSuma(suma,erori):
    '''
    functia valideaza suma ca fiind o suma pozitiva
    date in:suma,erori
    date out:-
    '''
    if checkSum(suma)==False:
        erori+="Suma trebuie sa fie pozitiva\n"
    verifErori(erori)
    
def validareTip(tip,erori):
    '''
    functia valideaza tipul care trebuie sa fie de intrare sau iesire
    date in:tip,erori
    date out:-
    '''
    if checkTip(tip)==False:
        erori+="Tipul nu este valid!Trebuie sa fie de intrare sau iesire\n"
    verifErori(erori)
    
def validareZiTxt(phrase):
    erori=""
    if checkInt(phrase)==True:
        zi=int(phrase)
        validareZi(zi,erori)
        return zi
    else:
        erori+="Comanda invalida"
    verifErori(erori)
    
def validareSumaTxt(phrase):
    erori=""
    if checkFloat(phrase)==True: 
        suma=float(phrase)
        validareSuma(suma, erori)
        return suma
    else:
        erori+="Comanda invalida"
    verifErori(erori)
    
