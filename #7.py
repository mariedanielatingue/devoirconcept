import string

def danie():
    mo=input("mete mo a ")
    indismo=[]
    for i in mo:
        indismo.append(str(string.ascii_letters.index(i)))
        
    print("_".join(indismo))
    

danie()