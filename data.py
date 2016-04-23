__table = []

def loadData():
    ROWS = 94671
    COLUMNS = 303
    
    val = []
    with open("data3.txt", "r") as f:
        val = f.readlines()
        val = [s.strip('\n') for s in val]

    for i in range(COLUMNS):
        wifi = [0 for k in range(ROWS)]
        __table.append(wifi)


    for i in range(ROWS):
        row = val[i].split(',')
        for k in range(COLUMNS):
            __table[k][i] = int(row[k])

def tableAt(i):
    return __table[i]
