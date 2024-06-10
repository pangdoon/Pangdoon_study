sik = input()


sik_buho_left = []
sik_buho_right = []
sik_number = []


for i in range(len(sik)):
    if sik[i] == "(":
        sik_buho_left.append((i, "("))
    elif sik[i] == ")":
        sik_buho_right.append((i, ")"))
    else:
        sik_number.append((i, sik[i]))

sik_buho_left.sort(reverse=True)


result = sik_number + sik_buho_left + sik_buho_right



print(sorted(result))
