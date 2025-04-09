from statistics import mean

mine = []
number = 1
while True :  
    i = 1
    while i < 20:
        
        # print(i)
        next_nummber = number % i
        if next_nummber != 0:
            number += 1
            mine =[]
            i = 1
            
            continue
            
        else: 
            mine.append(next_nummber)
        # print(mine)
        i += 1 
        
    if mean(mine) == 0 :
        print(number)
        break
    

    
        