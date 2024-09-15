module = [1.5, 2.5]
moduleE1 = 1.5
moduleE2 = 2.5
entraxe = 93.75
reductionFinalMin = 0.135
reductionFinalMax = 0.145

#------------------------------------------------------------------------------------
nombreDent1 = list(range(17,500))
nombreDent2 = list(range(14,500))

#-------------check les combinaison de dents qui respect l'entraxe-------------------

coupleQuiRespectEntraxe = []
for unModule in module:
    for unNombreDeDentDeZ1 in nombreDent1:
        for unNombreDeDentDeZ2 in nombreDent2:
            if (unNombreDeDentDeZ1 * unModule + unNombreDeDentDeZ2 * unModule == entraxe * 2):
                coupleQuiRespectEntraxe.append([unModule, unNombreDeDentDeZ1, unNombreDeDentDeZ2])      

#------------garder les combinaison entiere entre elle--------------------------------
def gcd(a, b):
    if (a == 0 or b == 0): 
        return 0
    if (a == b): 
        return a
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)

couplePremierEntreEux = []
for unCoupleDeNombre in coupleQuiRespectEntraxe:
    if (gcd(unCoupleDeNombre[1], unCoupleDeNombre[2]) == 1):
        couplePremierEntreEux.append(unCoupleDeNombre)

#------------Calculer les rapport de red d'un couple--------------------------------

CoupleFinaux = []
for unCoupleDeNombre in couplePremierEntreEux:
    unCoupleDeNombre.append(unCoupleDeNombre[1] / unCoupleDeNombre[2])

for x in couplePremierEntreEux:
    print(*x)
    
for premierCouple in couplePremierEntreEux:
    for secondCouple in couplePremierEntreEux:
        if (premierCouple[3] * secondCouple[3] < reductionFinalMax and premierCouple[3] * secondCouple[3] > reductionFinalMin):
            CoupleFinaux.append([premierCouple, secondCouple, premierCouple[3] * secondCouple[3]])

for x in CoupleFinaux:
    print(*x)


#for x in CoupleFinaux:
    #print("M1 = {}   Z1 = {}   Z2 = {}       M2 = {}   Z3 = {}   Z4 = {}      K = {}".format(x[0][0], x[0][1], x[0][2], x[1][0], x[1][1], x[1][2], x[2]))

avecBonModule = []
for Couple in CoupleFinaux:
    if (Couple[0][0] == 1.5 and Couple[1][0] == 2.5):
        avecBonModule.append(Couple)

for x in avecBonModule:
    print("M1 = {}   Z1 = {}   Z2 = {}       M2 = {}   Z3 = {}   Z4 = {}      K = {}".format(x[0][0], x[0][1], x[0][2], x[1][0], x[1][1], x[1][2], x[2]))