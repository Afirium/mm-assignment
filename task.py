def print_logo(N):
    # Constraint: 2 < N < 10000
    if N < 2 or N > 10000 or not N & 1:
        print("N violates the restriction")
        return False

    S = F = K = N
    s1, s2 = [N * "-" if x % 2 == 0 else N * "*" for x in range(5)], []

    for row in range(N + 1):
        # Draw the line twice
        for _ in range(2):
            if row <= (N - 1) / 2:
                print("".join(s1), end="")
            elif row > (N - 1) / 2:
                print("".join(s2), end="")
        print()
        # First half (s1)
        if row <= (N - 1) / 2:
            for i in range(5):
                if i == 2:
                    s1[i] = (F - 2) * "-"
                elif i % 2 == 0:
                    s1[i] = (S - 1) * "-"
                else:
                    s1[i] = (K + 2) * "*"
            F -= 2
            S -= 1
            K += 2
            # Fill s2 before using
            if row + 1 > (N - 1) / 2:
                for i in range(7):
                    if i == 2 or i == 4:
                        s2.append("-")
                    elif i % 2 == 0:
                        s2.append(S * "-")
                    elif i == 3:
                        s2.append((K - 2) * "*")
                    else:
                        s2.append(N * "*")
                    F = 1
        # Second half (s2)
        if row > (N - 1) / 2:
            for i in range(7):
                if i == 3:
                    s2[i] = (K - 4) * "*"
                elif i == 2 or i == 4:
                    s2[i] = (F + 2) * "-"
                elif i % 2 == 0:
                    s2[i] = (S - 1) * "-"
                else:
                    s2[i] = N * "*"
            S -= 1
            F += 2
            K -= 2


print_logo(10)
