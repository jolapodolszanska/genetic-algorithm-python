import numpy as np
import genetic as gen
import matplotlib.pyplot as plt

liczba_osobnikow = 16
d_ch = 11     #dlugoć chromosomu
liczba_generacji = 200
prog_mutacji = 0.050

results = np.zeros((liczba_generacji,3))

populacja = gen.wylosuj_poczatkowe(liczba_osobnikow)

results[0] = gen.ocena_populacji(populacja)

for i in  range(1,liczba_generacji):

    jakosc_osobnikow =  gen.wartosci_funkcji_przynaleznosci(populacja)
    
    wycinek_kola_ruletki =  gen.kumulacja(jakosc_osobnikow)       
    
    populacja_do_operacji_genetycznych = gen.selekcja(populacja, wycinek_kola_ruletki)
    
    nowa_populacja = gen.krzyzowanie(populacja_do_operacji_genetycznych, d_ch)
    
    nowa_populacja = gen.mutacja(nowa_populacja, d_ch, prog_mutacji)
    
    nowa_populacja  = gen.binarne_na_int(nowa_populacja)
    
    results[i] = gen.ocena_populacji(nowa_populacja)
            
    print(str(i)+': ' +str(results[i,0]))
    
#plot metrics
plt.plot(results)
plt.show()


