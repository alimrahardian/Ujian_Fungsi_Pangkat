def pangkat(x, y):
    if(y==0): 
        return 1
    
    asal = 1
    for item in range(1, y+1):
        asal = asal * x
    return asal


print(pangkat(4,0))

  