#length find

i=[[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
j=0
while j<=4:
    k=0
    len1 = len(i[j])
    while k<len1:
        print(i[j][k] , end='')
        k=k+1
    j=j+1
    print(end='\n')    

#1
#12
#123
#1234
#12345