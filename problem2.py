n = 4000000
t_1 = 1
t_2 = 2
total = t_2

while t_1 + t_2 < n:
    t = t_1 + t_2
    t_1 = t_2
    t_2 = t
    total += t if (t % 2 == 0) else 0

print total
