import numpy as np
import matplotlib.pyplot as plt
from random import*


"""Initialisation"""
i:int=0 #temps
lx=[]
ly=[]
x = randint(0, 1000) #somme total mise au debut par les grand investisseur
print(x)
b=x
a=0 #crise
c=0 #compteur
d=365 #nb de jours


"""
L= #liquidité
M=L*P #marketcap poids total de la crypto 
p: #prix du token
si a(=acheteur) achete pour x token.
price impact pi= (x*p*100)/m
si achat p=p+(p*pi)/100
si vente p=p-(pi*p)/100"""

"""Programme"""
for i in range(d):
    if b>=x: #achète
        r = randint(50, 100) #nb aléatoire entre 0 et 1000
        x = x + r #somme des petis investisseurs mettant régulièrement la même somme
        ly.append(x) #liste des points
        lx.append(i) #liste du temps
        c = c + 1 
    if b<x: #vend
        rv = randint(0, 50)#nb aléatoire qui vend
        x = x - rv + r/2 #vend car ça devient benefique + r car il y a toujours les investisseurs a long termes
        ly.append(x)
        lx.append(i)
    if c >= 40: #trop bas trop longtemps
        for i in range(d):
            x=0
            ly.append(x)
            lx.append(i)   
            
    if i%100 ==int: #au fils du temps c'est plus vraiment périodique mais plutot tt les jours ( tous les jours ça ved tous les jours ça achéte)
        x = x - randint(500, 1000)
    if random() <= 0.0001: #facteur aléatoire (comme par exemple covid ou problème au sein du marché) qui entrainerait une crise proba 10%
        while a < 100:
            x = x - randint(50, 100) + r/2 #les personnes quand même confiantes ?
            a= a+1
            ly.append(x) #liste des points
            lx.append(i) #liste du temps
    if random() <= 0.00001: #coup d'euphorie ou annonce importante qui inciterait les investisseur à acheter
        while a < 100:
            x = x + randint(50, 100)
            a= a+1
            ly.append(x) #liste des points
            lx.append(i) #liste du temps        
    if x<b:
        c = c + 1 #compteur
    if b*100>x:
        x = x - randint(50, 100) + r/2 #les personnes quand même confiantes ?
        a= a+1
        ly.append(x) #liste des points
        lx.append(i)
        
        
    #if #si le marché est trop souvent bas il n'y a plus aucun acheteur        


plt.title('''Marché financier USD/Days''')
plt.xlabel('Days')
plt.ylabel('UDS')

x = np.linspace(0,i,len(lx)) #points x entre 
y = np.array(ly)
plt.plot(x, y)
plt.show() # affiche la figure a l'ecran

"""Les investisseurs"""
#Les personnes qui investissent à loong terme, petite somme par mois sans se soucier réelement de l'augmentation, rv
#Les personnes qui investissent à courts terme donc grosse somme direct puis vend petit à petit, 

"""La psychologie"""
#Hope, j'y crois je met beaucoup d'argent 
#Optimism, c'est réel ça monte
#Belief, j'suis confiant je met beacoup d'argent 
#Thrill, exictation j'achète en masse
#Euphorie, on est au pick, très confiant

#Complacency, je suis satisfait je commence à vendre une partie (pas tout et je me prépare pour la prochaine hausse) ou sinon je vend tout et je racheterais plus tard quand le coup sera plus petit
#Anxiety, j'ai tout vendu mais ça ne baisse pas bcp pk?
#Denial, 