import random
import math

# fasele oghlidosi

def distance(x1, y1, x2, y2):
    return float("%0.2f" % (math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))))

# *******************************
# age fasele shahr 0 nabud va dide nashode bud un ro joze min ha hesab
# mikone va dr nahayat min fasele ra bargardanede va an khane ra true (seen) mikond
def findShortestWay(shomareSotun):
    min = 10000
    rowNum = -1
    for j in range(n):
        if D[shomareSotun][j] != 0.0 and seeNode[j] == False:
            if min > D[shomareSotun][j]:
                min = D[shomareSotun][j]
                rowNum = j
    seeNode[rowNum] = True
    return rowNum


# ******************************

n = int(input('n ra vared konid: '))
mokhtasat = []
node = []
seeNode = []
# be tedade shahr ha ye list az false ha misaze ke yani shahr ha ro nadide
# be surate random x ,y entekhab mishavad
for i in range(n):
    mokhtasat.append(random.randint(5, 15))
    mokhtasat.append(random.randint(5, 15))
    node.append(mokhtasat)
    mokhtasat = []
    seeNode.append(False)

satr = []
D = []
for i in range(n):
    for j in range(n):
        satr.append(distance(node[i][0], node[i][1], node[j][0], node[j][1]))
    D.append(satr)
    satr = []
# print node
print('\nmokhtasate node ha :\n', node, end='\n\n')
print('distance :')
# print matrix
for i in range(n):
    for j in range(n):
        print(D[i][j], end='   ')
    print()

print('\nmasire entekhabi : ')
# ebteda miad sutune 0 ro mide va az inja kutah trin rah ro entekhab mikone va chap mikone age i =-1
# bud yani hame shahr ha dide shode va be shahre aval(1) bazmigrdd
i = findShortestWay(0)
print('shahre 1')
seeNode[0] = True
masireHarekat = []
masireHarekat.append(1)
while (True):
    if i == -1:
        print('shahre 1')
        masireHarekat.append(1)
        break
    else:
        print('shahre', i + 1)
        masireHarekat.append(i + 1)
        i = findShortestWay(i)
print(masireHarekat)
