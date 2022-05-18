#import log as l
import functions as f
#n = 28
#mod = 29
b = 100
#alpha = 2
#betta = 5
alpha = 2
betta = 228 #5
mod = 383 #29
n = 191
N = 100
i = 0
x = f.FastPow(alpha, b, mod)

def function(x, n):
    if x %3 == 1:
        return x
    elif x%3 ==0:
        return (2*x) %n
    elif x%3== 2:
        return (x+1)%n
arr_x = []
arr_x.append(x)
d = 0

while i < N:
    f_x = function(x, n)
    x = (x*f.FastPow(alpha,f_x, mod ))%mod
    d+=  f_x
    arr_x.append(x)
    i+=1
y= betta
arr_y = []
arr_y.append(y)

def check_if_end(arr_y, x):
    for y in arr_y:
        if y == x:
           return arr_y.index(y)
i = 0
d_n = 0
arr_d_n = []


while i < N:
    if check_if_end(arr_y, x):
        break
    f_y = function(y, n)
    y = (y*f.FastPow(alpha,f_y, mod ))%mod
    d_n+=  f_y
    arr_d_n.append(d_n)
    arr_y.append(y)
    i+= 1

print('arrays of x values ', arr_x)
print('arrays of y values ', arr_y)
print('arrays of d_n values ', arr_d_n)
print('d is ', d )
print('i is ', i )
x = (b+ d - arr_d_n[i-1]) % n
print('x is ', x)
result = f.FastPow(alpha, x, mod)
print('alpha** x mod p = ', result)

