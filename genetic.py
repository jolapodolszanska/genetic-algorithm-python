import numpy as np
import random
import math


def wylosuj_poczatkowe(ile):
    liczby = np.zeros(ile, dtype=int)     
    for i in range(0,ile):
        liczby[i] = random.randrange(1,2047)
    return liczby

#konwersja z int na postać binarną
def zmien_na_binarne(tablica, dlugosc_kodu):
    liczby_binarne = []
    for i in range(0,len(tablica)):
        liczby_binarne.append(bin(tablica[i])[2:].zfill(dlugosc_kodu))
    return liczby_binarne

#wartoć funkcji przynależnoci dla osobnika x
def funkcja_przynaleznoci(x):
    return math.exp(-((math.sin(x)+2)**2-3*(math.sin(x)+2))-math.cos(x*6.28/2048))

# wektor wartosci funkcji przynależnoci dla wszystkich osobników w populacji 'tab'
def wartosci_funkcji_przynaleznosci(tab):
    wartosc_przynaleznosci = np.zeros(len(tab))
    for i in range(0,len(tab)):
        wartosc_przynaleznosci[i] = funkcja_przynaleznoci(tab[i])
    return wartosc_przynaleznosci

#wektor przypisujący osobnikowi częsć pola koła ruletki
def kumulacja(tab):
    res = np.zeros(len(tab))
    suma = np.sum(tab)
    res = np.zeros(len(tab))
    for i in range(0,len(tab)):
        res[i] = tab[i]/suma
    for i in range(1,len(tab)):
        res[i] += res[i-1]
    return res

#selekcja osobników do nowej rozmnożenia
def selekcja(stara_populacja, waznosc):
    nowa_populacja = np.zeros(len(stara_populacja), dtype=int)
    for i in range(0,len(stara_populacja)):
        foo = random.random()
        for j in range(0,len(stara_populacja)):
            if(foo<waznosc[j]):
                nowa_populacja[i] = stara_populacja[j]
                break
    return nowa_populacja
        
#ocena populacji
def ocena_populacji(stara_populacja):   
    tab = wartosci_funkcji_przynaleznosci(stara_populacja)
    return np.mean(tab), np.max(tab), stara_populacja[np.argmax(tab)]

#działanie krzyzowania
def krzyzowanie(populacja, dlugosc_kodu):
    binarne =  zmien_na_binarne(populacja, dlugosc_kodu)
    nowe_binarne = []
    if(len(binarne)%2==0):
        for i in range(0,len(populacja),2):
            foo1 = binarne[i]
            foo2 = binarne[i+1]
            podzial = random.randint(0,dlugosc_kodu)
            nowe_binarne.append(foo1[0:podzial]+foo2[podzial:len(foo2)])            
            nowe_binarne.append(foo2[0:podzial]+foo1[podzial:len(foo2)])
    else:
        for i in range(0,len(populacja)-1,2):
            foo1 = binarne[i]
            foo2 = binarne[i+1]
            podzial = random.randint(0,dlugosc_kodu)
            nowe_binarne.append(foo1[0:podzial]+foo2[podzial:len(foo2)])           
            nowe_binarne.append(foo2[0:podzial]+foo1[podzial:len(foo2)])
        nowe_binarne.append(binarne[len(populacja)-1])
    return nowe_binarne                    

#działeanie mutacji
def mutacja(populacja, dlugosc_kodu, tr):
    for i in range(0,len(populacja)):
        fuu = list(map(int, populacja[i]))
        for j in range(0,dlugosc_kodu):
            foo = random.random()
            if(foo<tr):
                fuu[j] = (fuu[j]+1)%2
        populacja[i] = ''.join(str(bit) for bit in fuu)        
    return populacja

# zmiana wartosci binarnych na liczby całkowite
def binarne_na_int(tab):
    nowa_tab = np.zeros(len(tab))
    for i in range(0,len(tab)):
        nowa_tab[i] = int(tab[i],2) 
    return nowa_tab 
       
