import string
import random
from random import *
numerique=string.digits
alfa=string.ascii_letters

def kodaleyatwa():
    n=alfa+numerique
    m=randint(2,61)
    kod=""
    for i in range(m):
        chif=randint(0,61)
        if n[chif] in kod:
            chif=randint(0,61)
        else:    
            kod+=n[chif]
        
    print(kod)


kodaleyatwa() 