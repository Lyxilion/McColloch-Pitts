def binaryToDec(x: list):
    """
        Convertit une chaine binaire en décimal
    :param x: une liste binaire
    :return: le nombre converti
    :rtype: int
    """
    y=0
    for i in range(len(x)) :
        y += x[i] * 2**(len(x)-1-i)
    return y
def decToBinary(x: int ):
    """
        Convertit un nombre décimale en liste binaire
    :param x: un entier
    :return: une liste binare
    :rtype: list
    """
    L = []
    while x // 2 != 0:
        if (x % 2 == 1):
            L.append(1)
        else:
            L.append(0)
        x = x // 2
    if (x % 2 == 1):
        L.append(1)
    else:
        L.append(0)

    return (list(reversed(L))) #on retourne une liste inversé

def intToList(x:int) :
    """
        décompose un int en list de nombre
    :param x: un nombre
    :return: une list du nombre 
    :rtype: list
    """
    return list(map(int, str(x)))

def listToInt(l:list):
    """
        Converti uen list en un nombre  
    :param l: une liste de nombre
    :return: un nombre
    :rtype: int
    """
    y = 0
    for i in range(len(l)):
        y += l[i] * 10 ** (len(l) - 1 - i)
    return y
def sgn(x:float):
    """
        La fonction sign
    :param x: un nombre
    :return: 1 ou 0
    :rtype: int
    """
    if x<0:
        return 0
    else :
        return 1
def f(X:list,H:list,t:int):
    """
        fontion de tranfert de McColloch-Pitts
    :param X: list : Connexion ativatrice
    :param H: list : Connexion inhibitrice
    :param t: int :seuil d'activation
    :return: la réponse du neurone
    :rtype: bool
    """
    x = 0
    h = 0
    for i in range(len(X)):
        x += X[i]
    for i in range(len(H)):
        h += H[i]
    if h == 0 :
        return sgn(x - t)
    else :
        return 0


def F_OU(I1, I2, I3):
    return f([I1, I2, I3], [0], 1)
def F_ET1(I1, I2, I3):
    return f([I1, I2, I3], [0], 2)
def F_ET2(I1, I2,I3):
    return f([I1, I2, I3], [0], 3)
def F_TEMP1(I1, I2):
    return f([I1], [I2], 1)
def F_TEMP2(I1):
    return f([I1], [0], 1)
def F_OUT(I1, I2):
    return f([I1, I2], [0], 1)

def Layer_1(X, OUT):
    OUT[0] = F_OU(X[0], X[1], OUT[1])
    OUT[2] = F_ET2(X[0], X[1], OUT[1])
    OUT[1] = F_ET1(X[0], X[1], OUT[1])
    return OUT
def Layer_2(OUT):
    OUT_Temp = [None,None]
    OUT_Temp[0] = F_TEMP1(OUT[0], OUT[1])
    OUT_Temp[1] = F_TEMP2(OUT[2])
    return OUT_Temp
def Layer_3(OUT):
    return F_OUT(OUT[0], OUT[1])

Ch_1 = None
Ch_2 = None
bool = False
while not bool :
    Ch_1 = input('Chaine n° 1 : ')
    Ch_2 = input('Chaine n° 2 : ')
    if len(Ch_1) == len(Ch_2) :
        bool = True
    else :

        print("Erreur : Les deux chaine doivent avoir la même longueur")
X = [[0], [0]]                                      #Liste qui contiendra les deux chaines binaires à Additioner
result = [0]
for i in range(len(Ch_1)):
    X[0].append(int(Ch_1[i]))
    X[1].append(int(Ch_2[i]))
    result.append(0)
print("X0",len(X[0]),"X1", len(X[1]),"result", len(result))

OUT_1 = [0, 0, 0]                                   #Le 1er Layer dispose d'une boucle, on initialise donc les sorties initiales à 0
Y = [None, None]                                    #Contiendras les deux bits qui seront additioner
for i in range(len(result)) :
    Y[0] = X[0][len(result)-1-i]                    #On commence par les bit de poids faible, soit ceux en bout de liste
    Y[1] = X[1][len(result)-1-i]
    OUT_1 = Layer_1(Y, OUT_1)                       #Liste contenant les resultat du 1er layer
    OUT_2 = Layer_2(OUT_1)                          #Résutat du 2em Layer
    result[len(result)-i-1] = Layer_3(OUT_2)        #On obtien la somme en sortie du layer 3, en commencent par les bits de poid faible


print("\n * Résultats :")
print(Ch_1," + " , Ch_2 ," = ", result)
print(binaryToDec(intToList(Ch_1))," + " , binaryToDec(intToList(Ch_2)) ," = ", binaryToDec(result))
