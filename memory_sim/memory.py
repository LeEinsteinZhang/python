mem = [None] * 256

def mem_manage():
    pass

def to(n):
    return mem[n]

def at(n):
    return mem.index(n)

print(mem)
print(to(128))
