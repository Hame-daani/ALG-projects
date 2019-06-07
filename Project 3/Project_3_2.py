squares = {}


def cutmin(a, b):
    # base case
    if a == b:
        if f"{a}*{b}" in squares:
            squares[f"{a}*{b}"] += 1
        else:
            squares[f"{a}*{b}"] = 1
        return
    m = min(a, b)
    if f"{m}*{m}" in squares:
        squares[f"{m}*{m}"] += 1
    else:
        squares[f"{m}*{m}"] = 1
    if a > b:
        return cutmin(a-m, b)
    else:
        return cutmin(a, b-m)


if __name__ == "__main__":
    a = int(input("Input A: "))
    b = int(input("Input B: "))
    cutmin(a, b)
    print(squares)
