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


"""
                     _ README _ 

Pour commencer, nous allons construire un réseau de neurones Feedforward pour créer un additionneur binaire de deux bits.
Il contient en tout 5 neurones et deux layer. Mais comme c'est un feedfoward, j'ai simplement à faire un imbriquent
de fonctions e transfère pour que cela me donne le résultat.

OUT[0] = f([X[0],X[1]],[0],2) #un neurone "ET" renvoie 1 si les deux entrées sont 1, donne le 2em bit du résultat
OUT[1] = f([f([X[0]],[0],1),f([X[1]],[0],1)],[OUT[0]],1) #un neurone "OU" entre les deux entré et le résultat du neurone précédent en inhibiteur

Donc :
si les deux entrés son null, les deux neurones renvoient 0 sur les deux bits
si une des deux et vrais, le neurone ET ne st pas activés donc renvoie 0 sur le 2e m bit, Et n'inhibe pas le neurone "OU" qui renvoie 1 sur le premier bit et le
Si les deux sont vrai, le neurone ET renvoient 1 sur le 2e m bit et inhibe le neurone OU qui renvoie 0 sur le 1er bit
"""

print("----------------------START----------------------")
OUT = [None,None]
print('Additioneur Binaire V1')
X = [0, 0]
OUT[0] = f([X[0],X[1]],[0],2) #un neurone "ET" renvoie 1 si les deux entrées sont 1, donne le 2em bit du résultat
OUT[1] = f([f([X[0]],[0],1),f([X[1]],[0],1)],[OUT[0]],1) #un neurone "OU" entre les deux entré et le résultat du neurone précédent en inhibiteur
print(X[0], "+", X[1], "=",OUT[0],OUT[1])

X = [0, 1]
OUT[0] = f([X[0],X[1]],[0],2)
OUT[1] = f([f([X[0]],[0],1),f([X[1]],[0],1)],[OUT[0]],1)
print(X[0], "+", X[1], "=",OUT[0],OUT[1])

X = [1, 0]
OUT[0] = f([X[0],X[1]],[0],2)
OUT[1] = f([f([X[0]],[0],1),f([X[1]],[0],1)],[OUT[0]],1)
print(X[0], "+", X[1], "=",OUT[0],OUT[1])

X = [1, 1]
OUT[0] = f([X[0],X[1]],[0],2)
OUT[1] = f([f([X[0]],[0],1),f([X[1]],[0],1)],[OUT[0]],1)
print(X[0], "+", X[1], "=",OUT[0],OUT[1])

print("-----------------------END-----------------------")

"""
                                    _ README _ 
                                    
Pour la suite, je vais créer un nouveau réseau pour faire la même chose, mais cette fois-ci sur un réseau qui possède une boucle ce n'est plus un simple réseau Feedforward. Et comme les informations ne "circulent" plus à la même vitesse,
(des interconnexions entre neurones d'un même layer) je dois obligatoirement modéliser chaque neurone et chacun layer
(je ne peux plus simplement faire un imbriquent de fonction). Et faire évoluer le réseau dans le temps.

"""
print("----------------------START----------------------")

def Add_Binaire2(X) :
    """
        
        Cette fonction modélise un additionneur Binaire de deux bits en utilisant un réseau de neuronne sur le model de McCulloch-Pitts.
        Elle n'utilise que 3 neurones graissaient à un système de retenue.
        Comme on a un seul bit en sortie du réseau et que notre résultat est une chaine, on obtient notre résultat au cours du temps.

    :param X: (List, leng 2, O or 1) Les bits a additioner 
    :return: list la chaine binaire de l'addtion chaine binaire
    """
    #__Functions__
        #CREATION DES NEURONES
    def F_OU(I1, I2, I3):
        """
            Neurone 'OU' avec 3 entrées
        :param I1: activator
        :param I2: activator
        :param I3: activator
        :return: int 0 or 1
        """
        return f([I1, I2, I3], [0], 1)
    def F_ET(I1, I2):
        """
            neurone 'ET' avec 2 entrées
        :param I1: activator
        :param I2: activator
        :return: int 0 or 1
        """
        return f([I1, I2], [0], 2)
    def F_OUT(I1, I2):
        """
            Neurone de Sortie 2 entrées
        :param I1: activator
        :param I2: inhibitor 
        :return: int 0 or 1
        """
        return f([I1], [I2], 1)

        #CREATION DES LAYERS
    def Layer_1(X, OUT):
        """
            Le premier Layer constitué du neurone OU et ET
            Au moment t0 :
            La sortie du neurone ET en t=t0-1 en entrée du OU (d'ou l'interet de la boucle)
            
        :param X: (List, leng 2, O or 1) Les bits à additioner 
        :param OUT: Les sortie du layer 1 a modifier
        :return: modification du OUT
        """
        OUT[0] = F_OU(X[0], X[1], OUT[1])
        OUT[1] = F_ET(X[0], X[1])
        return OUT
    def Layer_2(OUT):
        """
            Le second layer composé du neurone OUT
        :param OUT: Les sorties du Layer 1
        :return: 0 or 1
        """
        return F_OUT(OUT[0], OUT[1])

    #__CORE__
        #Création des Var
    OUT = [0,0] #Sorte du layer_1 [0] -> OU / [1] -> ET
    result = [None,None] #Sortie du Layer_2 au court du temps

        #boucle dans les layers
    for i in range(2) :
        if i == 1 :
            X = [0, 0]
        OUT = Layer_1(X, OUT)
        result[1-i] = Layer_2(OUT)

    return result


print('Additioneur Binaire V2')
X = [0, 0]
R = Add_Binaire2(X)
print(X[0], "+", X[1], "=",R[0], R[1])
X = [0, 1]
R = Add_Binaire2(X)
print(X[0], "+", X[1], "=",R[0], R[1])
X = [1, 0]
R = Add_Binaire2(X)
print(X[0], "+", X[1], "=",R[0], R[1])
X = [1, 1]
R = Add_Binaire2(X)
print(X[0], "+", X[1], "=",R[0], R[1])

print("-----------------------END-----------------------")
