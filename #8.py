import string
alfabe=string.ascii_letters

index= input("entre index")
mot=[]

for i in index.split("-"):
    mot.append(alfabe[int(i)])

print("".join(mot))





