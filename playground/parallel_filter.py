from functools import reduce


xs = [1,2,3,4]
ys = [5,6,7,8]
zs = [9,10,11,12]

def combination_(r, l):
    return r + l

def even_(acc, nxt):
    if nxt %2 == 0:
        return acc + [nxt]
    else: return acc

resx = reduce(even_, xs, [])
resy = reduce(even_, ys, [])
resz = reduce(even_, zs, [])

combined = combination_(combination_(resx, resy), resz)
print(combined)


