#Var cst----------------------------------------------------
MODULE1 = 1.5
MODULE2 = 2.5
ENTRAXE = 93.75
REDUCTIONFINAL = 0.14
PRECISIONREDUCTION = 0.005

nombreDentRoue = list(range(17,500)) 
nombreDentPignon = list(range(17,500))

#fonction utile---------------------------------------------
def respecteEntraxe(entraxe, module, z1, z2): 
    return (module * (z1 + z2) / 2 == entraxe)

def gcd(a, b):
    if (a == 0 or b == 0): 
        return 0
    if (a == b): 
        return a
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)

def afficherTab(tab):
    for x in tab:
        print("{:.1f} {:4d} {:4d}   {:.17f}".format(x[0], x[1], x[2], x[3]))
    print("")

def estDansIntervalReduction(reduction1, reduction2, reductionVoulue, precisionRed):
    return (reduction1 * reduction2 > reductionVoulue - precisionRed) and (reduction1 * reduction2 < reductionVoulue + precisionRed)

def formatText(tab):
    for x in tab:
        print("{:.1f} {:4d} {:4d}   {:.17f}   {:.1f} {:4d} {:4d}   {:.17f}      {:.17f}      {:.17f}".format(x[0][0], x[0][1], x[0][2], x[0][3], x[1][0], x[1][1], x[1][2], x[1][3], x[2], x[3]))
        
#Engrenage1 check entraxe et nbr dent coprime------------------------------------------------
tableauEngrenage1 = []
for dentRoue in nombreDentRoue:
    for dentPignon in nombreDentPignon:
        if dentRoue > dentPignon :
            if respecteEntraxe(ENTRAXE, MODULE1, dentRoue, dentPignon) and (gcd(dentRoue, dentPignon) == 1):
                tableauEngrenage1.append([MODULE1, dentRoue, dentPignon, dentPignon/dentRoue])

afficherTab(tableauEngrenage1)

#Engrenage2 check entraxe et nbr dent coprime------------------------------------------------
tableauEngrenage2 = []
for dentRoue in nombreDentRoue:
    for dentPignon in nombreDentPignon:
        if dentRoue > dentPignon :
            if respecteEntraxe(ENTRAXE, MODULE2, dentRoue, dentPignon) and (gcd(dentRoue, dentPignon) == 1):
                tableauEngrenage2.append([MODULE2, dentRoue, dentPignon, dentPignon/dentRoue])

afficherTab(tableauEngrenage2)

#rapportRedValide------------------------------------------------
candidatValide = []
for red1 in tableauEngrenage1:
    for red2 in tableauEngrenage2:
        if estDansIntervalReduction(red1[3], red2[3], REDUCTIONFINAL, PRECISIONREDUCTION):
            candidatValide.append([red1, red2, red1[3]*red2[3], abs(red1[3] - red2[3])])

formatText(candidatValide)