
def flat_generator(l):
    a=0
    b=0
    while a < len(l):
        while b < len(l[a]):
            item = l[a][b]
            b += 1 
            yield from [item]
        a += 1
        b = 0
              
