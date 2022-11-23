
def smooth(l):
    if not l:
        return []
    elif type(l[0]) == list:
            return smooth(l[0]) + smooth(l[1:])
    return [l[0]] + smooth(l[1:])