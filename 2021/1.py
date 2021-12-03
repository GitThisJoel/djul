word = input().split()
def get_num(h):
    b = ""
    for c in h:
        if c.isupper():
            b += "1"
        else:
            b += "0"
    return str(int(b,2))
out = ""
for l in word:
    n = ""
    for p in l.split('-'):
        n += get_num(p)
    out += chr(int(n,8))
print(out)
