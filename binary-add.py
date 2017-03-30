def sgn(x):
    if x<0:
        return 0
    else :
        return 1

def f(X,H,t):
    """
        fontion de tranfert de McColloch-Pitts
    :param X: list : Connexion ativatrice
    :param H: list : Connexion inhibitrice
    :param t: int :seuil
    :return: Bool
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
Pour commencer, nous allons construire un reseau de neurone FeedForward pour creer un additioneur binaire de deux bits.
Il contient en tout 5 neuronnes et deux layer. Mais comme c'est un feedfoward, j'ai simplement à faire un imbriquement
de fonctiond e transfert pour que cela me donne le resultat.

OUT[0] = f([X[0],X[1]],[0],2) #un neurone "ET" renvoie 1 si les deux entrées sont 1, donne le 2em bit du resultat
OUT[1] = f([f([X[0]],[0],1),f([X[1]],[0],1)],[OUT[0]],1) #un neurone "OU" entre les deux entré et le resultat du neurone précedent en inibiteur

Donc :
 si les deux entré sont null, les deux neurone renvoie 0 sur les deux bits
 si une des deux et vrai, le neurone ET n'est pas activerdonc renvoie 0 sur le 2em bit, Et n'inhibe pas le neurone "OU" qui renvoi 1 sur le premier bit et le 
 Si les deux sont vrai, le neurone ET renvoie 1 sur le 2em bit et inhibe le neurone OU qui renvoie 0 sur le 1er bit
 
"""
print("----------------------START----------------------")
OUT = [None,None]
print('Additioneur Binaire V1')
X = [0, 0]
OUT[0] = f([X[0],X[1]],[0],2) #un neurone "ET" renvoie 1 si les deux entrées sont 1, donne le 2em bit du resultat
OUT[1] = f([f([X[0]],[0],1),f([X[1]],[0],1)],[OUT[0]],1) #un neurone "OU" entre les deux entré et le resultat du neurone précedent en inibiteur
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
                                    
Pour la suite, je vais creer un nouveau reseau pour faire la meme chose, mais cetet foix-ci sur un reseau qui possede une boucle
 ce n'est plus un simple réseau FeedForward. Et comme les insformation ne "circulent" plus a la même vitesse,
(des interconnexion entre neurone d'un même layer) je dois obligatoirement modeliser chaque neurone et chaque layer
(je ne peux plus simplement faire un imbriquement de fonction). Et faire évoluer le réseau dans le temps.

"""
print("----------------------START----------------------")

def Add_Binaire2(X) :
    """
        Cette fonction modelise un additioneur Binaire de deux bits en utilisant un reseau de neuronne sur le modelle de McCulloch-Pitts.
        Elle n'utilise que 3 neuronnes grace a un systeme de retenue.
        Comme on a un seul bit en sortie du reseau et que notre resultat est une chaine, on aobtien notre resultat au cours du temps.
        
    :param X: (List, leng 2, O or 1) Les bits a additioner 
    :return: list la chaine binaire de l'addtion chaine binaire
    """
    #__Functions__
        #CREATION DES NEURONES
    def F_OU(I1, I2, I3):
        """
            Neurone 'OU' avec 3 entrees
        :param I1: activator
        :param I2: activator
        :param I3: activator
        :return: int 0 or 1
        """
        return f([I1, I2, I3], [0], 1)
    def F_ET(I1, I2):
        """
            neurone 'ET' avec 2 entrees
        :param I1: activator
        :param I2: activator
        :return: int 0 or 1
        """
        return f([I1, I2], [0], 2)
    def F_OUT(I1, I2):
        """
            Neurone de Sortie 2 entres
        :param I1: activator
        :param I2: inhibitor 
        :return: int 0 or 1
        """
        return f([I1], [I2], 1)

        #CREATION DES LAYERS
    def Layer_1(X, OUT):
        """
            Le premier Layer constituer du neurone OU et ET
            Au moment t0 :
            La sortie du neurone ET en t=t0-1 en entré du OU (d'ou l'interet de la boucle)
            
        :param X: (List, leng 2, O or 1) Les bits a additioner 
        :param OUT: Les sortie du layer 1 a modifier
        :return: modification du OUT
        """
        OUT[0] = F_OU(X[0], X[1], OUT[1])
        OUT[1] = F_ET(X[0], X[1])
        return OUT
    def Layer_2(OUT):
        """
            Le second layer composer du neurone OUT
        :param OUT: Les sorties du Layer 1
        :return: 0 or 1
        """
        return F_OUT(OUT[0], OUT[1])

    #__CORE__
        #Creation des Var
    OUT = [0,0] #Sorte du layer_1 [0] -> OU / [1] -> ET
    result = [None,None] #Sortie du Layer_2 au court du temps

        #boucle dans les layers
    for i in range(2) :
        if i == 1 :
            X = [0, 0]
        Layer_1(X, OUT)
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
