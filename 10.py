
def loudine():
    non=input("mete non anh")
    chan=[]
    init=""
    for i in non:
        non=non.replace(" ","-")
        
    for i in non.split("-"):
        chan.append(i)   
        
    for i in chan:
        init+=i[0]         
    print(init)    