# s= "This iss a python language"

# words = s.split()

# even_words = [w for w in words if (len(w)%2==0)]

# result = " ".join(even_words)

# print(result)

#Using generator expression with map

a = "geeks for geeks"

words = a.split()

even_words = [w for w in words if (len(w)%2==0)]

even_wrd_str = map(str, even_words)

res = " ".join(even_wrd_str)

print(res)

#Using for loop

a = "My name is Nitin"

words = a.split()

for w in words:
    if len(w)%2==0:
        print(w, end=" ")
        
