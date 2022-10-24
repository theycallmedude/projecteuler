c = 998
b = 500
a = 500

# check_arr = []

while c > 0:
    c = c - 1
    while b > 0: 
        b = b - 1
        while a > 0:
            if a + b + c == 1000 and (a**2 + b**2) == c**2:
                check_arr = [a,b,c]
            a = a - 1
        a = b - 1
    b = c - 1

print(check_arr)

ans = 1

for i in check_arr:
    ans = ans * i

print(ans)

