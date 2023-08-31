def is_balanced(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the bracket sequence
    s = input()

    if not is_balanced(s):
        print("NO")
    else:
        print("YES")
        n = len(s)
        t = "(" + s + ")" + "()" * (n // 2)
        print(t)