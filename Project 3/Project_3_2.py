squares = {}


def cutmin(a, b):
    # base case: we cut 1 square and we finish the paper.
    if a == b:
        if f"{a}*{b}" in squares:
            squares[f"{a}*{b}"] += 1
        else:
            squares[f"{a}*{b}"] = 1
        return
    
    # we only can cut square as size as minimum edge.
    m = min(a, b)
    # we cut a square with size of m
    if f"{m}*{m}" in squares:
        squares[f"{m}*{m}"] += 1
    else:
        squares[f"{m}*{m}"] = 1
    # go recursive to what left from paper.
    return cutmin(a-m, b) if a > b else cutmin(a, b-m)


if __name__ == "__main__":
    a = int(input("Input A: "))
    b = int(input("Input B: "))
    cutmin(a, b)
    print(squares)
