def get_king_moves(s, t):
    dx = abs(ord(t[0]) - ord(s[0]))  # Horizontal distance
    dy = abs(int(t[1]) - int(s[1]))  # Vertical distance

    moves = max(dx, dy)  # Minimum number of moves

    print(moves)

    for _ in range(moves):
        move = ""
        if t[0] > s[0]:
            s = chr(ord(s[0]) + 1) + s[1]  # Update the x-coordinate
            move += "R"
        elif t[0] < s[0]:
            s = chr(ord(s[0]) - 1) + s[1]  # Update the x-coordinate
            move += "L"
        if t[1] > s[1] or ((t[1] > s[1]) and t[0] == s[0]):
            s = s[0] + str(int(s[1]) + 1)  # Update the y-coordinate
            move += "U"
        elif t[1] < s[1] or ((t[1] < s[1]) and t[0] == s[0]):
            s = s[0] + str(int(s[1]) - 1)  # Update the y-coordinate
            move += "D"

        print(move)

# Read the input
s = input().strip()
t = input().strip()

# Call the function to get the king's moves
get_king_moves(s, t)