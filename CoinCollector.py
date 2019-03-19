def horizontal_tail(coins, index, N):
    j = index
    while j < N and coins[j]:
        j += 1
    return j-1


def horizontal_collect(coins, index, tail):
    while index <= tail:
        coins[index] -= 1
        index += 1


def collect(coins, index, N):
    if index >= N:
        return 0, ""
    elif coins[index] == 0:
        return collect(coins, index+1, N)
    else:
        v_result = coins[index]
        h_tail = horizontal_tail(coins, index, N)
        h_result = h_tail - index+1
        if v_result > h_result:
            coins[index] = 0
            num_moves, moves = collect(coins, index+1, N)
            return num_moves + 1, f"V {index+1}\n"+moves
        if h_result >= v_result:
            horizontal_collect(coins, index, h_tail)
            num_moves, moves = collect(coins, index, N)
            return num_moves+1, f"H {index+1} {h_tail+1}\n"+moves


def min_step_collect(stack):
    return collect(stack, 0, len(stack))


if __name__ == "__main__":
    number_of_columns = 5
    stack = [2, 1, 2, 5, 1]
    num_moves, moves = min_step_collect(stack)
    print(num_moves)
    print(moves)
