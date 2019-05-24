from pandas import DataFrame


def findMin(costs):
    """
    return minimum between our 5 operation costs.
    """
    minKey = list(costs.keys())[0]
    minValue = list(costs.values())[0]
    for key, value in costs.items():
        if value < minValue and value > 0:
            minKey = key
            minValue = value
    return minKey, minValue


def findAnswer(x, y, op_costs):
    """
    main func that return two array for total cost and operations followed to that cost.
    
    input:
        x: source string
        y: target string
        costs: dic include each operation's cost.
    """

    # initial the arrays
    total_costs = [[0 for j in range(0, len(x)+1)] for i in range(0, len(y)+1)]
    moves = [[0 for j in range(0, len(x)+1)] for i in range(0, len(y)+1)]
    total_costs[0][0] = 0
    moves[0][0] = 0
    # fill first row and first column for converting x to null string,and null to y string.
    # converting x to null: require only delete operation.
    # converting null to y: is done with insert operation.
    for i in range(1, len(x)+1):
        total_costs[0][i] = i * op_costs['del']
        moves[0][i] = f"del {x[i-1]}"
    for j in range(1, len(y)+1):
        total_costs[j][0] = j * op_costs['ins']
        moves[j][0] = f"ins {y[j-1]}"
    # main loop to fill our two array
    for i in range(1, len(y)+1):
        for j in range(1, len(x)+1):
            costs = {}
            # we could use copy operation only when two character be the same.
            # otherwise we use replace operation.
            if x[j-1] == y[i-1]:
                costs['cp'] = op_costs['cp'] + total_costs[i-1][j-1]
            else:
                costs['rep'] = op_costs['rep'] + total_costs[i-1][j-1]
            if i >= 2 and j >= 2 and x[j-1] == y[i-2] and x[j-2] == y[i-1]:
                costs['tw'] = op_costs['tw'] + total_costs[i-2][j-2]
            costs['del'] = op_costs['del'] + total_costs[i][j-1]
            costs['ins'] = op_costs['ins'] + total_costs[i-1][j]
            # find minimum between this operations.
            minKey, minValue = findMin(costs)
            total_costs[i][j] = minValue
            if minKey == 'del' or minKey == 'cp':
                moves[i][j] = minKey + f" {x[j-1]}"
            elif minKey == 'ins':
                moves[i][j] = minKey + f" {y[i-1]}"
            else:
                moves[i][j] = minKey + f" {x[j-1]}-{y[i-1]}"

    return total_costs, moves


def prettyPrint(x, y, costs, moves):
    """
    pretty printing our two array.
    """
    print("----------------------")
    print(DataFrame(data=costs, index=[0]+list(y), columns=[0]+list(x)))
    print("----------------------")
    print(DataFrame(data=moves, index=[0]+list(y), columns=[0]+list(x)))
    print("----------------------")


def find(moves, n, m):
    """
    return string includes all moves to convert x[0:n] to y[0:m]
    input:
        moves: array includes operations that we fill with dynamic programing.
    """
    # base case.
    if n == 0 and m == 0:
        return ""
    if moves[n][m].startswith('cp') or moves[n][m].startswith('rep'):
        return find(moves, n-1, m-1) + "\n"+ moves[n][m]
    if moves[n][m].startswith('del'):
        return find(moves, n, m-1) + "\n"+ moves[n][m]
    if moves[n][m].startswith('ins'):
        return find(moves, n-1, m) + "\n"+moves[n][m]
    if moves[n][m].startswith('tw'):
        return find(moves, n-2, m-2)+ "\n"+moves[n][m]


def readData(filename):
    """
    read and retun a dic include opertion costs from a file.
    """
    with open(filename) as f:
        data = f.readlines()
    op_costs = {}
    op_costs["cp"] = int(data[0].rstrip('\n'))
    op_costs["rep"] = int(data[1].rstrip('\n'))
    op_costs["del"] = int(data[2].rstrip('\n'))
    op_costs["ins"] = int(data[3].rstrip('\n'))
    op_costs["tw"] = int(data[4].rstrip('\n'))
    return op_costs


def getAnswer(total_costs, total_moves):
    """
    return final cost and string include all moves needed.
    """
    # our final cost is in last cell
    cost = total_costs[len(y)][len(x)]
    moves = find(total_moves, len(y), len(x))
    return cost, moves


if __name__ == "__main__":
    op_costs = readData('in.txt')
    print(DataFrame.from_dict(op_costs,orient='index',columns=[""]))
    x = input("Input source string: ")
    y = input("Input target string: ")

    totalcosts, totalmoves = findAnswer(x, y, op_costs)
    
    cost, moves = getAnswer(totalcosts, totalmoves)

    print("\nAnswer is: ", cost)
    print("\nWith this moves:",end="")
    print(moves)

    prettyPrint(x, y, totalcosts, totalmoves)
