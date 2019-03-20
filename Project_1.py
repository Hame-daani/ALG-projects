
def find_min(coins, low, high):
    min = low
    while(low <= high):
        if coins[low] <= coins[min]:
            min = low
        low += 1
    return min


def h_pop(coins, low, high, n):
    for a in range(n):
        for b in range(low, high+1):
            coins[b] -= 1
    return coins


def collect(coins, low, high):
    if low == high:
        if coins[low]:
            return 1, f"V {low+1}\n"
    if low > high:
        return 0, ""

    minimum = find_min(coins, low, high)
    v_result = high - low + 1
    h_result = coins[minimum]
    coins = h_pop(coins, low, high, h_result)
    h_moves = ""
    for a in range(h_result):
        h_moves += f"H {low+1} {high+1}\n"
    left_result, left_moves = collect(coins, low, minimum-1)
    right_result, right_moves = collect(coins, minimum+1, high)
    h_result += left_result+right_result
    if v_result < h_result:
        v_moves = ""
        for a in range(low, high+1):
            v_moves += f"V {a+1}\n"
        return v_result, v_moves
    elif h_result <= v_result:
        h_moves += left_moves
        h_moves += right_moves
        return h_result, h_moves


def min_step_collect(coins):
    return collect(coins=coins, low=0, high=len(coins)-1)


if __name__ == "__main__":
    number_of_columns = 5
    coins = [2, 1, 2, 5, 1]
    num_moves, moves = min_step_collect(coins)
    print(num_moves)
    print(moves)
