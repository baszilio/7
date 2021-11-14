def merge(*lists):
    lio=[]
    for poki in range(len(lists)):
        lio +=lists[poki]
    lio.sort()
    return print(lio)
