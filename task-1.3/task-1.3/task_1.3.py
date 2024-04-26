x = float(input())
y = float(input())
a = x + y
b = x - y
c = x * y
d = x / y 
e = x // y
print(a,b,c,d,e)
cur_max1, cur_max2 = a, b # 5 3
if a < b: cur_max1, cur_max2 = a, b
if c >= cur_max1:
    cur_max2 = cur_max1
    cur_max1 = c
else:
    if c > cur_max2:
        cur_max2 = c
if d >= cur_max1:
    cur_max2 = cur_max1
    cur_max1 = d
else:
    if d > cur_max2:
        cur_max2 = cur_max1
        cur_max2 = d
if e >= cur_max1:
    cur_max2 = cur_max1
    cur_max1 = e
else:
    if e > cur_max2:
        cur_max2 = e
print(cur_max1, cur_max2)

    