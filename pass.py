# pass by value , function argument 

def myfunct(a):
    for i in a:
        print(i,a[i])

pgdca = {"div":"A","sem":"2"}
myfunct(pgdca)        

# div A
# sem 2