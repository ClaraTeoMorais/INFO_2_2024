print("Digite uma frase:")

frase = []

f = input().split()

frase.append(f)

print(frase)

for x in range (len(frase)):
    frase = frase[1:]
    print (frase)

# s = input("Digite uma frase: ") + " "
# for k in range (len(s)):
#     if s[k] == " ": 
#         print (s[k-1], end = "")
# print()

