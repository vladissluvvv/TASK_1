x = float(input())
y = float(input())
a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
cur_max = a
if b > cur_max: cur_max = b
if c > cur_max: cur_max = c
if d > cur_max: cur_max = d
if e > cur_max: cur_max = e
print(cur_max)