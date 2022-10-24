import math

start = 2000000

def is_prime(num):

    sq_num = int(math.sqrt(num))

    if num == 2:
        return(True)

    if num % 2 == 0:
        return(False)

    for check in range(3,sq_num+1,2):
        if num % check == 0:
            return(False)

    return(True)

ans = 0

for num in range(2,start):
    if is_prime(num):
        ans = ans + num

print(ans)