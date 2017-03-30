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
Fonctionnement :
    Un neurone est representer par une fonction de tranfert, qui prend trois argument : 
        -Une liste des conexion activatrices
        -Une liste des connexion inhibitrices
        -Un seuile
    Le seuile correspond au nombre de connexion activatrice qui doivent être active pour que le neurone renvoie 1
    Si une seule connexion inhibitrice est vrai, le neurone renvoie 0
"""
"""
Modelisation de la fonction répondant a cette table de vérite :
 _________________
| Entre | Sorties |
|_________________|
|  001  |   1     |
|  011  |   1     |
|  101  |   1     |
|  111  |   1     |
| Sinon |   0     |
|_________________|
"""

X=[0,0,1]
print(f(                            #Si une des 4 chaine est trouver, renvoie 1
    [
        f([X[2]],[X[0],X[1]],1),   # reconnait la chaine '001'
        f([X[1],X[2]],[X[0]],2),   # reconnait la chaine '011'
        f([X[0],X[2]],[X[1]],2),   # reconnait la chaine '101'
        f([X[0],X[1],X[2]],[0],3)  # reconnait la chaine '111'
    ]
, [0], 1))

X=[0,1,1]
print(f(
    [
        f([X[2]],[X[0],X[1]],1),
        f([X[1],X[2]],[X[0]],2),
        f([X[0],X[2]],[X[1]],2),
        f([X[0],X[1],X[2]],[0],3)
    ]
, [0], 1))
X=[1,0,1]

print(f(
    [
        f([X[2]],[X[0],X[1]],1),
        f([X[1],X[2]],[X[0]],2),
        f([X[0],X[2]],[X[1]],2),
        f([X[0],X[1],X[2]],[0],3)
    ]
, [0], 1))
X=[1,1,1]

print(f(
    [
        f([X[2]],[X[0],X[1]],1),
        f([X[1],X[2]],[X[0]],2),
        f([X[0],X[2]],[X[1]],2),
        f([X[0],X[1],X[2]],[0],3)
    ]
, [0], 1))
X=[1,1,0]

print(f(
    [
        f([X[2]],[X[0],X[1]],1),
        f([X[1],X[2]],[X[0]],2),
        f([X[0],X[2]],[X[1]],2),
        f([X[0],X[1],X[2]],[0],3)
    ]
, [0], 1))
