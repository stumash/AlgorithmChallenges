from random import randint

def createSquareMatrix(n, intrange=(1,9)):
    return [
        [randint(intrange[0], intrange[1]) for _ in range(n)]
        for _ in range(n)
    ]

# in place
def rotateMatrix(m):
    for layer in range(len(m) // 2):
        for elemNum in range(layer, len(m)-layer-1):

            i, j = layer, elemNum
            coords = [
                (i,j),
                (j,len(m)-1-i),
                (len(m)-1-i,len(m)-1-j),
                (len(m)-1-j,i)
            ]
            tempvals = [m[row][col] for row,col in coords]
            tempvals = [tempvals[-1]] + tempvals[:-1]

            for (i,j),v in zip(coords, tempvals):
                m[i][j] = v

def printMatrix(m):
    for row in m:
        print(",".join([str(x) for x in row]))
    print()


def test():
    m =  [
        ['a','a','b','b'],
        ['a','a','b','b'],
        ['d','d','c','c'],
        ['d','d','c','c']
    ]
    printMatrix(m)
    rotateMatrix(m)
    printMatrix(m)
    print()
    m2 =  [
        ['a','a','b','b','b'],
        ['a','a','b','b','b'],
        ['d','d','c','c','c'],
        ['d','d','c','c','c'],
        ['d','d','c','c','c']
    ]
    printMatrix(m2)
    rotateMatrix(m2)
    printMatrix(m2)
