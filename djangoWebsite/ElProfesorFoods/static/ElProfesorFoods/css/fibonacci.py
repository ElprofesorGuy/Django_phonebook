def fibonacci(nbre):
    if(nbre==1 or nbre==0):
        return 1
    else:
        return fibonacci(nbre-1) + fibonacci(nbre-2) 
    

nbre = 6;
print(fibonacci(6))