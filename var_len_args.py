# variable length argument

def main(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
main(10,20,30,40,50,60,70,80,90)   

#450     