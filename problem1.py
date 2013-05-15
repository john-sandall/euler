n = 1000
total = 0

def addMultiples(x,multiplier):
    for i in range( 1 , ((n-1) / multiplier)+1 ):
        x = x + multiplier*i
    return x
    
total = addMultiples(total,3)
total = addMultiples(total,5)

print total