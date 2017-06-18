import random as rdm
def binaryToDec(x: list):
    """
        Converti une chaine binaire en décimal
    :param x: une liste binaire
    :return: le nombre converti
    :rtype: int
    """
    y = 0
    for i in range(len(x)):
        y += x[i] * 2 ** (len(x) - 1 - i)
    return y


def decToBinary(x: int):
    """
        Converti un nombre décimale en liste binaire
    :param x: un entier
    :return: une liste binaire
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

    return (list(reversed(L)))  # on retourne une liste inversé


def Network(L1: list, L2: list):
    """
        Le réseau de neurone, qui additionne deux chaine binaires et renvoie le modulo 4 de la somme
    :param L1: Une chaine binaire
    :param L2: Une chaine binaire
    :return: le modulo 4 de la somme
    :rtype: int
    """

    def sgn(x: float):
        """
            La fonction sign
        :param x: un nombre
        :return: 1 ou 0
        :rtype: int
        """
        if x < 0:
            return 0
        else:
            return 1

    def f(X: list, H: list, t: int):
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
        if h == 0:
            return sgn(x - t)
        else:
            return 0

    # Definition des neurones
    def F_OU(I1, I2, I3):
        return f([I1, I2, I3], [0], 1)

    def F_ET1(I1, I2, I3):
        return f([I1, I2, I3], [0], 2)

    def F_ET2(I1, I2, I3):
        return f([I1, I2, I3], [0], 3)

    def F_TEMP1(I1, I2):
        return f([I1], [I2], 1)

    def F_TEMP2(I1):
        return f([I1], [0], 1)

    def F_OUT(I1, I2):
        return f([I1, I2], [0], 1)

    def F_END1(I1):
        return f([I1], [0], 1)

    def F_END2(I1, I2):
        return f([I1], [I2], 1)

    # Définition des couches
    def Layer_1(X, OUT):
        OUT[0] = F_OU(X[0], X[1], OUT[1])
        OUT[2] = F_ET2(X[0], X[1], OUT[1])
        OUT[1] = F_ET1(X[0], X[1], OUT[1])
        return OUT

    def Layer_2(OUT):
        OUT_Temp = [None, None]
        OUT_Temp[0] = F_TEMP1(OUT[0], OUT[1])
        OUT_Temp[1] = F_TEMP2(OUT[2])
        return OUT_Temp

    def Layer_3(OUT):
        return F_OUT(OUT[0], OUT[1])

    def Layer_4(OUT, Old_OUT):
        OUT_Temps = [None, None]
        OUT_Temps[0] = F_END1(OUT[0])
        OUT_Temps[1] = F_END2(Old_OUT[0], OUT[0])
        return OUT_Temps

    X = [[0], [0]]  # Liste qui contiendra les deux chaines binaires à Additioner
    result = [0]
    for i in range(len(L1)) :
        X[0].append(L1[i])
        X[1].append(L2[i])
        result.append(0)
    # CALCUL DE LA SOMME

    OUT_1 = [0, 0, 0]  # Le 1er Layer dispose d'une boucle, on initialise donc les sorties initiales à 0
    Y = [None, None]  # Contiendras les deux bits qui seront additioner
    for i in range(len(result)):
        Y[0] = X[0][len(result) - 1 - i]
        Y[1] = X[1][len(result) - 1 - i]
        OUT_1 = Layer_1(Y, OUT_1)
        OUT_2 = Layer_2(OUT_1)
        result[len(result) - i - 1] = Layer_3(OUT_2)
        # On obtien la somme en sortie du layer 3, en commencent par les bits de poid faible
    # CALCUL DU MODULO 4
    X = result
    return f(  # Si une des 4 chaine est trouver, renvoie 1
        [
            f([X[1]], [X[0], X[2], X[3]], 1),  # reconnait la chaine '0101'
            f([X[0]], [X[1], X[2], X[3], ], 1),  # reconnait la chaine '1000'
        ]
        , [0], 1)


def decide():
    """
        Prédiction du meilleur coup a jouer
    :return: le nombre de baton a prendre
    :rtype: int
    """
    nbr_vide = 0  # On compte le nombre d'espaces vides
    for e in Game:
        if e == 0:
            nbr_vide += 1
    nbr_vide = decToBinary(nbr_vide)  # on converti le nombre décimal en binaire
    temps = [0, 0, 0]  # la chaine binaire doit avoir une longueur de 3
    for i in range(len(nbr_vide)):
        temps[len(temps) - 1 - i] = nbr_vide[
            len(nbr_vide) - 1 - i]  # on rempli donc la liste vide avec les valeurs de nbr_vide

    Possible = [[0, 0, 1],  # les 3 coups possibles
                [0, 1, 0],
                [0, 1, 1]]
    for i in range(len(Possible)): # On teste chaque coup possible
        if Network(Possible[i], temps) == 1:  # Si le modulo 4 de la somme des espaces vides et du nombre de batons à enlever vaut 1, le coup est gagant

            return binaryToDec(Possible[i])  # On retourne la valeur du coup gagnant

    return 1  # Si aucun des coups n'est gagants, on enlève 1 baton pour retarder la défaite


# ---- JEUX ---- #

def showGame():
    """
        Affiche le plateau de jeux
    :return: None
    """
    print("| ", end='')
    for i in Game:
        print(i, end=' | ')
    return None


def play(x: int):
    """
        Joue une manche.
    :param x: un nombre entier entre 1 et 3 de batons à prendre
    :return: le nouveau plateau de jeux
    :rtype: list
    """
    L = Game[:]
    for i in range(len(L)):
        if L[i] == 1 and x != 0:  # On vérifie que cette case contient un baton, et qu'il reste des batons a prendre
            L[i] = 0
            x -= 1
    return L


def countBaton():
    """
        Compte le nombre de batons restant en jeux
    :return: le nombre de batons restant
    :rtype: int
    """
    sum = 0
    for e in Game:
        if e == 1:  # On compte le nombre de 1 dans la liste Game
            sum += 1
    return sum

stat = []
loop = 10000
turn = 1 #1 : IA start | 0 : player start
for i in range(loop):
    Game = [1, 1, 1, 1, 1, 1, 1, 1, 1]  # stock la situation actuel du plateau de jeu
    nbr_manche = 0  # nombre de manches
    win = False  # condition de victoire
    winner = None
    while not win:
        if nbr_manche % 2 == turn:  # Tour du joueur
            if countBaton() == 0 :  # Vérification de victoire
                win = True
                winner = 0
            else:
                rand = rdm.randint(1,3)
                Game = play(rand)  # Demande du nombre de batons à jouer
        else:  # Tour de l'IA
            if countBaton() == 0:  # Vérification de victoire
                win = True
                winner = 1
            else:
                nbr_baton = decide()  # Calcul de nombre de batons à jouer
                Game = play(nbr_baton)
        nbr_manche += 1  # Incrément du nombre de manches
    stat.append(winner)
    if i % 100 == 0:
        print("Partie n°",i,sep="")

summ = 0
for e in stat :
    if e == 1 :
        summ+=1
print("L'IA a un pourcentage de victoire de : ", 100 *summ/loop,"%", sep="")