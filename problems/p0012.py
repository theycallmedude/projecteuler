import math
import numpy as np

def check_divisors(num):
    check_size = 0
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            check_size = check_size + 1
    return check_size*2

# check = 0
# it = 1

# while check_divisors(it) <= 500:
#     check = check + it
#     it = it + 1 

# print(check)

# print(it)

print(check_divisors(5040))