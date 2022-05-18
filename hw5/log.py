import functions as f
import pandas as pd
def check_to_which_S(x):
    if x < 9.66:
        return 1
    elif x <  19.33:
        return 2
    elif x < 29:
        return 3
def check_to_which_S_v2(x):
    if x %3 == 1:
        return 1
    elif x%3 ==0:
        return 2
    elif x%3== 2:
        return 3
def count_a(a_i, numb_S, n):
    if numb_S == 1:
        return a_i
    elif numb_S == 2:
        return (2*a_i)%n
    elif numb_S == 3:
        return (a_i+1) % n
def count_b(b_i, numb_S, n):
    if numb_S == 1:
        return (b_i +1) % n
    elif numb_S == 2:
        return (2*b_i)%n
    elif numb_S == 3:
        return b_i

def count_x(a_i, b_i, alpha, betta, mod):
    x = (alpha**(a_i) * betta**(b_i )) % mod
    return x
def find_same(arr):
    for i in  range(len(arr)//2):
        if arr[i] == arr[2*i] and i != 0:
            return i
    return 'no'
x= 1
a = 0
b = 0
arr_x = [-1, x]
arr_a = [-1, a]
arr_b = [-1, b]
alpha = 2
betta = 228 #5
mod = 383 #29
n = 191 #28
while find_same(arr_x) == 'no':
    numb_S = check_to_which_S_v2(x) #!!!!!
    a = count_a(a, numb_S, n)
    b = count_b(b, numb_S, n)
    x = count_x(a, b, alpha, betta, mod)
    arr_b.append(b)
    arr_x.append(x)
    arr_a.append(a)
print('arrays of x values ', arr_x[1:])
print('arrays of a values ', arr_a[1:])
print('arrays of b values ', arr_b[1:])
i =find_same(arr_x)
print('i is ', i )
r = (arr_b[i] - arr_b[2*i]) % n
print('r is ', r)
t = f.gcd(r,n)
if r == 0 or f.gcd(r,n)!= 1:
    x = 22

else:
    r1 =f.get_minus(r, n)
    print('r-1 is ', r1)
    diff_a = (arr_a[2*i] - arr_a[i])%n
    x = (r1* diff_a ) % n
    print('x is ', x)
result = f.FastPow(alpha, x, mod)
print('alpha** x mod p = ', result)

