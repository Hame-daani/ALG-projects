def readDebts(filename):
    debts = {}
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            l = l.rstrip('\n')
            debt, giver, getter = l.split()
            if giver in debts:
                debts[giver] -= int(debt)
            else:
                debts[giver] = -1*int(debt)
            if getter in debts:
                debts[getter] += int(debt)
            else:
                debts[getter] = int(debt)
    return debts


if __name__ == '__main__':
    debts = readDebts('in.txt')
