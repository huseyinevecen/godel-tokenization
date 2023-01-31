def cantor_pair(a, b):
    return (a + b) * (a + b + 1) // 2 + b

def cantor_unpair(z):
    w = int(((8 * z + 1) ** 0.5 - 1) / 2)
    t = (w ** 2 + w) // 2
    b = z - t
    a = w - b
    return (a, b)

# use the Cantor pairing function to define the encoding
stoi = { ch:cantor_pair(i, len(chars)) for i,ch in enumerate(chars) }
itos = { cantor_pair(i, len(chars)):ch for i,ch in enumerate(chars) }

encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

print(encode("hii there"))
print(decode(encode("hii there")))