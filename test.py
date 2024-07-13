def l_algo(s="A", n=5):
    if n == 0:
        return s
    arr_s = []
    for char in s:
        if char == "A":
            arr_s.append("AB")
        elif char == "B":
            arr_s.append("A")
    s = "".join(arr_s)
    return l_algo(s, n - 1)


print(l_algo(n=36))
