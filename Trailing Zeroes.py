def trailing(n):
    count=0
    c=5
    while(n/c>=1):
        count+=int(n/c)
        c*=5
    return count
if __name__=="__main__":
    x=[3,60,100,1024,23456,8735373]
    for n in x:
        print(trailing(n))