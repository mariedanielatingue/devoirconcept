import string 
import random
from random import *


def kodaleyatwa():
    n=string.ascii_letters
    m=randint(2,61)

    kod=""
    for i in range(m):
        let=randint(0,25)
        if n[let] in kod:
            let=randint(0,25)
        else:    
            kod+=n[let]
        
    print(kod)


kodaleyatwa() 