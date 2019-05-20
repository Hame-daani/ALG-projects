def findMin(cost):
    minKey = 1000000
    minValue = 1000000
    for key, value in cost.items():
        if value < minValue and value > 0:
            minKey = key
            minValue = value
    return minKey, minValue


def findAnswer(x, y, costs):
    t_cost = [[0 for j in range(0, len(x)+1)] for i in range(0, len(y)+1)]
    moves = [[0 for j in range(0, len(x)+1)] for i in range(0, len(y)+1)]
    t_cost[0][0] = 0
    moves[0][0] = 0
    # initial the arrays
    for i in range(1, len(x)+1):
        t_cost[0][i] = i*costs['del']
        moves[0][i] = f"del {x[i-1]}"
    for j in range(1, len(y)+1):
        t_cost[j][0] = j*costs['ins']
        moves[j][0] = f"ins {y[j-1]}"
    for i in range(1, len(y)+1):
        for j in range(1, len(x)+1):
            cost = {}
            if x[j-1] == y[i-1]:
                cost['cp'] = costs['cp'] + t_cost[i-1][j-1]
                cost['rep'] = 0
            else:
                cost['cp'] = 0
                cost['rep'] = costs['rep'] + t_cost[i-1][j-1]
            if i >= 2 and j >= 2 and x[j-1] == y[i-2] and x[j-2] == y[i-1]:
                cost['tw'] = costs['tw']+t_cost[i-2][j-2]
            else:
                cost['tw'] = 0
            cost['del'] = costs['del'] + t_cost[i][j-1]
            cost['ins'] = costs['ins'] + t_cost[i-1][j]
            minKey, minValue = findMin(cost)
            t_cost[i][j] = minValue
            # moves[i][j] = minKey + \
            #     f" {x[j-1]} {y[i-1]}" if minKey == 'tw' else minKey+f" {x[j-1]}"
            if minKey == 'tw':
                moves[i][j] = minKey + f" {x[j-1]} {y[i-1]}"
            if minKey == 'cp' or minKey == 'del':
                moves[i][j] = minKey + f" {x[j-1]}"
            else:
                moves[i][j] = minKey + f" {y[i-1]}"

    return t_cost, moves


def prettyPrint(x, y, cost, moves):

    for row in cost:
        for column in row:
            print(column, end='\t')
        print()
    print("-----")
    for row in moves:
        for column in row:
            print(column, end='\t')
        print()


def find(moves, n, m):
    if n == 0 and m == 0:
        return ""
    if moves[n][m].startswith('cp') or moves[n][m].startswith('rep'):
        return find(moves, n-1, m-1)+"\n"+moves[n][m]
    if moves[n][m].startswith('del'):
        return find(moves, n, m-1)+"\n"+moves[n][m]
    if moves[n][m].startswith('ins'):
        return find(moves, n-1, m)+"\n"+moves[n][m]
    if moves[n][m].startswith('tw'):
        return find(moves, n-2, m-2)+"\n"+moves[n][m]


# x = input("Input source string: ")
# y = input("Input target string: ")
# costs = {}
# costs["cp"] = int(input("input copy costs: "))
# costs["rep"] = int(input("input replace costs: "))
# costs["del"] = int(input("input delete costs: "))
# costs["ins"] = int(input("input insert costs: "))
# costs["tw"] = int(input("input twiddle costs: "))
x = "alta"
y = "alat"
costs = {}
costs["cp"] = 3
costs["rep"] = 6
costs["del"] = 7
costs["ins"] = 5
costs["tw"] = 6

t_cost, moves = findAnswer(x, y, costs)
prettyPrint(x, y, t_cost, moves)
cost = t_cost[len(y)][len(x)]
move = find(moves, len(y), len(x))
print()
print(cost)
print (move)
