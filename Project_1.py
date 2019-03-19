def horizontal_tail(coins, index, N):
    # find next column that is empty. cause its the tail of our horizontal collection.
    j = index
    while j < N and coins[j]:
        j += 1
    return j-1


def horizontal_collect(coins, index, tail):
    while index <= tail:
        coins[index] -= 1
        index += 1


def vertical_collect(coins, index):
    coins[index] = 0


def collect(coins, index, N):
    if index >= N:  # base case: reaching end of columns.
        return 0, ""
    elif coins[index] == 0:
        # if column is empty, go to next column.
        return collect(coins, index+1, N)
    else:
        # vertical collecting result is equal to 'column height'.
        v_result = coins[index]
        h_tail = horizontal_tail(coins, index, N)
        h_result = h_tail - index + 1
        if v_result > h_result:
            vertical_collect(coins, index)
            # we go to the next column.
            num_moves, moves = collect(coins, index+1, N)
            return num_moves + 1, f"V {index+1}\n"+moves
        if h_result >= v_result:
            horizontal_collect(coins, index, h_tail)
            # we stay at current column.
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
