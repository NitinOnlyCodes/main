#usinf list comprehension

s = "hello world"
w=s.split()
res = " ".join([
    i[0].upper() + i[1:-1] + i[-1].upper()
    if len(i) > 1 else i.upper()
    for i in w
])

print(res)

# using map

s1 = "welcome to papa k paneer shop"

res1 = ' '.join(map(
    lambda word : word[0].upper() + word[1:-1] + word[-1].upper()
    if len(word) > 1 else word.upper(), s1.split()
))
print(res1)