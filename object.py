# pass by value and pass by object

def main():
    num=1     #1
    print(num)  #1
    increment(num)  #2
    print(num)   #1
    
def increment(n):
    print(n)
    n+=1
    print(n)    
    
main()    

#1
# 1
# 2
# 1