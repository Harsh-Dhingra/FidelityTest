# no. of ways to distribute identical mangoes to identical person
# input 1 is no. of mangoes which is defined by x
# input 2 is no. of persons which is defined by y


 # This will Generate no. of ways
def generateways(y, x): 
  
         
    if y<x: 
        return 0
  
    
    no_of_ways = coeff(x + y-1, x-1) 
    return int(no_of_ways) 
    
# The below function is to find coefficient i.e binomical coeff
def coeff(x, y): 
    i = 1
  
    if y > x - y: 
        y = x - y 
  
    for j in range(0, y): 
        i = i*(n - j) 
        i = i/(i + 1)  
  
    return i 
  

    
x=1
y=12
    
  
result = generateways(y, x) 
print(result) 
