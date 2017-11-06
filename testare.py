'''
Created on Nov 1, 2017

@author: Monica
'''
from validare import *
from util import *
from functionalitati import *
from domeniu import *
from menus import *
import uiInt

def test_validareTranzactie():
    try:
        tr={}
        setZi(tr,30)
        setSuma(tr,100)
        setTip(tr,"intrare")
        validareTranzactie(tr)
        assert(True)
    except valueError:
        assert(False)
    try:
        tr={}
        setZi(tr,30)
        setSuma(tr,100)
        setTip(tr,"0")
        validareTranzactie(tr)
        assert(False)
    except ValueError:
            assert(True)
        
def test_checkZi():
    assert checkZi(1)==True
    assert checkZi(40)==False

def test_checkSum():
    assert checkSum(1)==True
    assert checkSum(-410)==False
        
def test_checkTip():
    assert checkTip("intrare")==True
    assert checkTip("0")==False
    
def test_adauga():
    l=[]
    adauga(l,10)
    assert l[0]==10
    
def test_adaugaLista():
    l=[]
    adaugaLista(l,['a','b'])
    assert l[0]==['a','b']
    
def test_adaugaTranzactie():
    lista=[]
    adaugaTranzactie(lista,12,100,"iesire")
    assert getZi(lista[0])==12
    assert getSuma(lista[0])==100
    assert getTip(lista[0])=="iesire"
    
def test_stergereTranzactieZi():
    l=[]
    adaugaTranzactie(l,1, 100,"intrare")
    adaugaTranzactie(l,10,10,"iesire")
    assert(stergeTranzactieZi(l,1)==True)
    assert(stergeTranzactieZi(l,2)==False)

        
def test_stergeTranzactiePerioada():
    l=[]
    adaugaTranzactie(l,1, 100, "intrare")
    adaugaTranzactie(l,2, 100, "intrare")
    assert(stergeTranzactiePerioada(l,1,2)==True)
    assert(stergeTranzactiePerioada(l,4,2)==False)
    
def test_stergeTranzactieTip():
    l=[]
    adaugaTranzactie(l,1,100,"intrare")
    assert(stergeTranzactieTip(l,"intrare")==True)
    assert(stergeTranzactieTip(l, "iesire")==False)
    
def test_sumaTotala():
    l=[]
    adaugaTranzactie(l,12,10,'intrare')
    adaugaTranzactie(l,20,30,'intrare')
    assert(sumaTotalaTrAcelasiTip(l, 'intrare')==40)
    assert(sumaTotalaTrAcelasiTip(l, 'iesire')==0)
    
def test_verificareExistentaZi():
    l=[]
    adaugaTranzactie(l,12,10,'intrare')
    assert(verificareExistentaZi(l, 12)==True)
    assert(verificareExistentaZi(l, 1)==False)
   
def test_soldCont():
    l=[]
    adaugaTranzactie(l,12,10,'iesire')
    adaugaTranzactie(l,12,111,'intrare')
    assert(soldCont(l,12)==101)
    
def test_eliminaTranzactiiSumaData():
    l=[]
    adaugaTranzactie(l,12,10,'intrare')
    adaugaTranzactie(l,12,111,'intrare')
    adaugaTranzactie(l,13,10,'intrare')
    assert(eliminaTranzactiiSumaData(l,10)==True)
    assert(eliminaTranzactiiSumaData(l,100)==False)
    
def test_eliminaTranzactiiMaiMiciSuma():
    l=[]
    adaugaTranzactie(l,12,10,'intrare')
    adaugaTranzactie(l,12,111,'intrare')
    adaugaTranzactie(l,13,20,'intrare')
    assert(eliminaTranzactiiMaiMiciSuma(l, 30, 'intrare')==True)
    assert(eliminaTranzactiiMaiMiciSuma(l, 34, 'intrare')==False)
    
def test_undo():
    info={}
    setLista(info,[])
    setUndo(info,[])
    setPhrase(info,"")
    adaugaTranzactie(getLista(info),12,10,'intrare')
    setUndo(info,adaugaListaUndo(info))
    adaugaTranzactie(getLista(info),12,111,'intrare')
    setUndo(info,adaugaListaUndo(info))
    info=uiInt.undo(info)
    newL=[]
    adaugaTranzactie(newL, 12,10,'intrare')
    assert(getLista(info)==newL)
    
def runTests():
    test_validareTranzactie()
    test_checkZi()
    test_checkSum()
    test_checkTip()
    test_adaugaTranzactie()
    test_adauga()
    test_adaugaLista()
    test_stergereTranzactieZi()
    test_stergeTranzactiePerioada()
    test_stergeTranzactieTip()
    test_sumaTotala()
    test_verificareExistentaZi()
    test_soldCont()
    test_eliminaTranzactiiSumaData()
    test_eliminaTranzactiiMaiMiciSuma()
    test_undo()
    
