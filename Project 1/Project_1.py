def find_min(coins, low, high):
    # return 'index' with 'minimum height'.
    min = low
    while(low <= high):
        if coins[low] <= coins[min]:
            min = low
        low += 1
    return min


def h_pop(coins, low, high, n):
    # 'n' time 'pop' from columns in range of 'low' to 'high'.
    for a in range(n):
        for b in range(low, high+1):
            coins[b] -= 1
    return coins


def collect(coins, low, high):
    # base case
    if low > high:
        return 0, ""

    # finding minimum height. it will be our halfing point.
    minimum = find_min(coins, low, high)

    # vertical moves number is equal to columns number.
    v_result = high - low + 1
    v_moves = ""
    for a in range(low, high+1):
        v_moves += f"V {a+1}\n"

    # horizontal moves number is equal to minimum height that we found.
    h_result = coins[minimum]
    h_moves = ""
    coins = h_pop(coins, low, high, h_result)
    for a in range(h_result):
        h_moves += f"H {low+1} {high+1}\n"

    # halfing coins from minimum index into left and right part.
    left_result, left_moves = collect(coins, low, minimum-1)
    right_result, right_moves = collect(coins, minimum+1, high)

    h_result += left_result + right_result
    h_moves += left_moves + right_moves
    if v_result < h_result:
        return v_result, v_moves
    else:
        return h_result, h_moves


def min_step_collect(coins):
    return collect(coins=coins, low=0, high=len(coins)-1)


if __name__ == "__main__":
    # get input from user in format: "2 5 4 1"
    coins = [int(c) for c in input("Input number of coins in each column: ").split()]
    num_moves, moves = min_step_collect(coins)
    print(num_moves)
    print(moves)
