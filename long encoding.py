#wwxyzwww->23#(2)24#25#26#23#(3)


a='wwxyzwww'
out=''
n=len(a)
i=0
while i<n:
    c=1
    while i<n-1 and a[i]==a[i+1]:
        c+=1
        i+=1
    i+=1

    if (ord(a[i-1])-96) < 10:
        if c>1:
            out+=str(ord(a[i-1])-96)+'('+str(c)+')'
        else:
            out+=str(ord(a[i-1])-96)
    else:
        if c>1:
            out+=str(ord(a[i-1])-96)+'#'+'('+str(c)+')'
        else:
            out+=str(ord(a[i-1])-96)+'#'

print(out)