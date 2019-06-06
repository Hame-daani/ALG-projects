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
    return [{'name': key, 'debt': value} for key, value in debts.items()]


def itsSolution(debts):
    if not debts:
        return True
    return False


def select(debts):
    return debts[0], debts[-1]


def minimum(a, b):
    return a if a < b else b


if __name__ == '__main__':
    debts = readDebts('in.txt')
    sort_debts = sorted(debts, key=lambda x: x['debt'])

    net_amount = 0
    # solution check
    while not itsSolution(sort_debts):
        giver, getter = select(sort_debts)
        minDebt = minimum(-1*giver['debt'], getter['debt'])
        net_amount += minDebt
        print(f"{giver['name']} --{minDebt}--> {getter['name']}")
        if minDebt == -1*giver['debt']:
            sort_debts.pop(0)
        else:
            giver['debt'] += minDebt
        if minDebt == getter['debt']:
            sort_debts.pop(-1)
        else:
            getter['debt'] -= minDebt
