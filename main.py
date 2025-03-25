import matplotlib.pyplot as plt

# Transposition (Q1)
M = [[-1, 2,], 
     [0, 1],
     [3, 4]]

def transpose(M):
    result = []
    for j in range(len(M[0])):
        new_row = []
        for i in range(len(M)):
            new_row.append(M[i][j])
        result.append(new_row)
    return result

# Tracé d'une ligne (Q2)
def ligne(n,xmin,xmax):
    W=[]
    dx=(xmax-xmin)/(n-1)
    for x in range (n):
        W.append([x*dx,0,0])
    return(transpose(W))

#(X,Y,Z)=ligne(20,-5,5)

# Tracé d'un carré vide (Q3)
def carrevide(n, a):
    points_par_cote = (n + 3) // 4  # Arrondir pour garantir que l'on ait n points
    points = [] 

    for i in range(points_par_cote):
        x = a / 2 - i * (a / (points_par_cote - 1))
        points.append([x, -a / 2, 0])
        
    for i in range(points_par_cote):
        x = -a / 2 + i * (a / (points_par_cote - 1))
        points.append([x, a / 2, 0])

    for i in range(points_par_cote):
        y = a / 2 - i * (a / (points_par_cote - 1))
        points.append([a / 2, y, 0])
    
    for i in range(points_par_cote):
        y = -a / 2 + i * (a / (points_par_cote - 1))
        points.append([-a / 2, y, 0])
    
    points = points[:n] 
    # Séparer les coordonnées X, Y, Z
    X = [point[0] for point in points]
    Y = [point[1] for point in points]
    Z = [point[2] for point in points]

    return X, Y, Z

# Tracer l'exemple
n = 20  # Nombre de points
a = 10  # Longueur du côté du carré

X, Y, Z = carrevide(n, a)

# Affichage

# Q1
print(M)
print(transpose(M))

# Q2
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X, Y, Z, c=Z, cmap='ocean')

#fig, ax = plt.subplots(figsize=(6, 4))
#table = ax.table(cellText=transpose(M), loc='center', cellLoc='center')
#ax.axis('off')

plt.show()