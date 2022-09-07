import time
mulai = time.time()
def deretajaib(n) :  
    if n <= 5 : 
        return n
    else : 
        return deretajaib(n-2) + deretajaib(n//2)   


berehenti = time.time()

print(deretajaib(8), berehenti - mulai,"detik", )
 




#awal = [1,2,3,4,5] 
