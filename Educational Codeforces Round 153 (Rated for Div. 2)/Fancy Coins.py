# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the values of m, k, a1, and ak
    m, k, a1, ak = map(int, input().split())

    if k == 1:
        # If k is 1, we can only use the coins worth 1 burle
        total_coins_needed = (m + a1 - 1) // a1
    else:
        # Calculate the number of regular coins needed
        regular_coins_needed = (m - a1 + k - 2) // (k - 1)

        # Calculate the remaining cost after using regular coins
        remaining_cost = m - regular_coins_needed * a1

        # Calculate the number of fancy coins needed
        fancy_coins_needed = (remaining_cost + ak - 1) // ak

        # Calculate the total number of coins needed
        total_coins_needed = regular_coins_needed + fancy_coins_needed

    # Print the total number of coins needed
    print(total_coins_needed)