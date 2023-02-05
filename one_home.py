def decor(munk):
    def drapiz(*args):
        print(munk(*args) / len(args))

    return drapiz



@decor
def fdevv(*args):
    print(sum(args))
    return sum(args)


fdevv(1, 15, 23)








