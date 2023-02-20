n = int(input('Enter number of rows : '))
i = 1
while i <= n :
    j = 0
    while j <= i:
        j = j + 1
        if j == 2:
            continue
        print(j, end = " ")
    print("")
    i += 1
   
    
#o.p.    
#Enter number of rows : 5
#1
#1 3
#1 3 4
#1 3 4 5
#1 3 4 5 6