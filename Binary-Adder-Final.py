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


Ch_1 = input('Chaine n° 1 : ')
Ch_2 = input('Chaine n° 2 : ')
X = [[0], [0]]
result = [0]
for i in range(len(Ch_1)):
    X[0].append(int(Ch_1[i]))
    X[1].append(int(Ch_2[i]))
    result.append(0)


OUT_1 = [0, 0, 0]
OUT_2 = [0, 0]
Y = [None, None]
for i in range(len(result)) :
    Y[0] = X[0][len(result)-1-i]
    Y[1] = X[1][len(result)-1-i]
    OUT_1 = Layer_1(Y, OUT_1)
    OUT_2 = Layer_2(OUT_1)
    result[len(result)-i-1] = Layer_3(OUT_2)

print(result)
