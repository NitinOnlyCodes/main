s = "hello"

i = len(s)//2

res = s[:i].upper()+ s[i:]
print(res)

#using for loop

s1 = "hello world!"
res = ""
half_index = len(s1)//2

for i in range(len(s1)):
    if i < half_index:
        res += s1[i].upper()
    else:
        res += s1[i]
print(res)

#using list comprehension

s ="hello"
index=len(s)//2

res = "".join([s[i].upper() if i<index else s[i] for i in range(len(s))])
print(res)