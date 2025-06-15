s= "This iss a python language"

words = s.split()

even_words = [w for w in words if (len(w)%2==0)]

result = " ".join(even_words)

print(result)