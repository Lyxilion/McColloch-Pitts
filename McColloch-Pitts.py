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
Fonctionnement : 
    Un neurone est représenté par une fonction de transfert, qui prend trois arguments :
        -Une liste des connexions activatrices
        -Une liste des connexions inhibitrices
        -Un seuil
        le seuil correspond au nombre de connexion activatrice qui doit être active pour que le neurone renvoie 1 
        si une seule connexion inhibitrice est vraie, le neurone renvoyé 0
"""
"""
Modélisation de la fonction répondant à cette table de vérité :
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
print(f(                            #Si une des 4 chaines est trouvée, renvoie 1
    [
        f([X[2]],[X[0],X[1]],1),   # Reconnaît la chaine '001'
        f([X[1],X[2]],[X[0]],2),   # Reconnaît la chaine '011'
        f([X[0],X[2]],[X[1]],2),   # Reconnaît la chaine '101'
        f([X[0],X[1],X[2]],[0],3)  # Reconnaît la chaine '111'
    ]
    , [0], 1))
