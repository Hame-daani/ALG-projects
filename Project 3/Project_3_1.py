def readDebts(filename):
    """
    read data from file and return a list 
    include person name and net amout of debt.
    """
    debts = {}
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            l = l.rstrip('\n')
            debt, giver, getter = l.split()
            # add negative amount for giver
            if giver in debts:
                debts[giver] -= int(debt)
            else:
                debts[giver] = -1*int(debt)
            # add positive amount for getter
            if getter in debts:
                debts[getter] += int(debt)
            else:
                debts[getter] = int(debt)
    # convert to a list include {name,debt}
    return [{'name': key, 'debt': value} for key, value in debts.items()]


def itsSolution(debts):
    """
    check if we come with a solution or not.
    """
    if not debts:
        return True
    return False


def select(debts):
    """
    return min and max debts.
    """
    return debts[0], debts[-1]


if __name__ == '__main__':
    debts = readDebts('in.txt')
    # sorting debts from min to max.
    sort_debts = sorted(debts, key=lambda x: x['debt'])

    net_amount = 0
    # solution check
    while not itsSolution(sort_debts):
        # get giver and getter
        giver, getter = select(sort_debts)
        # find minimum between debt of two.
        minDebt = min(-1*giver['debt'], getter['debt'])
        # add it to net amount
        net_amount += minDebt
        # transit minDebt from giver to getter
        print(f"{giver['name']} --{minDebt}--> {getter['name']}")
        # subtract min from each debt
        # or pop it if its equal to min.
        if minDebt == -1*giver['debt']:
            sort_debts.pop(0)
        else:
            giver['debt'] += minDebt
        if minDebt == getter['debt']:
            sort_debts.pop(-1)
        else:
            getter['debt'] -= minDebt
