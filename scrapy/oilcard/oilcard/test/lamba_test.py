def make_add(n):
    return lambda x : [n,x,x+n]

f = make_add(5)
print f
print f(9)