def sumMultiples(multiplier,n):
    x = 0
    for i in range( 1 , ((n-1) / multiplier)+1 ):
        x = x + multiplier*i
    return x
    
total = sumMultiples(3,1000) + sumMultiples(5,1000) - sumMultiples(15,1000)
print total